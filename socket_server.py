
import time
import threading
import hashlib
import socket
import base64

# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



# 监听端口:
s.bind(('127.0.0.1', 9999))

s.listen(5)
print('Waiting for connection...')


def parse_headers(msg):
    headers = {}
    header, data = msg.split('\r\n\r\n', 1)
    # print("header == "+header)
    for line in header.split('\r\n')[1:]:
        key, value = line.split(': ', 1)
        headers[key] = value
    headers['data'] = data
    return headers


def generate_token(msg):
    # print("generate msg === "+msg)
    sStr = msg + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
    sha1 = hashlib.sha1()
    sha1.update(sStr.encode('utf-8'))
   # print("sha1 === " + sha1.hexdigest())

    token = base64.b64encode(sha1.digest())
    return token.decode("utf-8")

CODES = ['UTF-8', 'UTF-16', 'GB18030', 'BIG5',"GBK"]

# 获取字符编码类型
def string_encoding(b: bytes):
    """
    获取字符编码类型\n
    :param b: 字节数据\n
    :return: \n
    """
    # 遍历编码类型
    for code in CODES:
        try:
            b.decode(encoding=code)
            return code
        except Exception:
            continue
    return "noCode"

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    data = sock.recv(1024)
    data = data.decode('utf-8')
    headers = parse_headers(data)
    token = generate_token(headers['Sec-WebSocket-Key'])
    print("token == " + token)
    response = "HTTP/1.1 101 Switching Protocols\r\nUpgrade:websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: " + token + "\r\n\r\n"
    sock.send(response.encode("utf-8"))
    time.sleep(1)
    #headers = parse_headers(data)
    while True:
        try:
            data = sock.recv(1024)
        except socket.error:
            print("socket error")
            break
        if not data:
            print("no data")
            time.sleep(1)
            continue
        time.sleep(1)
        codetype = string_encoding(data)
        print("编码类型:", codetype)
        if(codetype == "noCode"):
            continue
        msg = data.decode(codetype)
        print("msg == ",msg)
        #sock.send(b'hello,world')
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()