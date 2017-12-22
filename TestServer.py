import threading
import hashlib
import socket
import base64
import time

global clients
clients = {}


# 通知客户端
def notify(message):
    for connection in clients.values():
        connection.send('%c%c%s' % (0x81, len(message), message))


# 客户端处理线程
class websocket_thread(threading.Thread):
    def __init__(self, connection, username):
        super(websocket_thread, self).__init__()
        self.connection = connection
        self.username = username

    def run(self):
        print('new websocket client joined!')
        data = self.connection.recv(1024)
        data = data.decode('utf-8')
        headers = self.parse_headers(data)
        token = self.generate_token(headers['Sec-WebSocket-Key'])
        print("token == "+token)
        response = "HTTP/1.1 101 Switching Protocols\r\nUpgrade:websocket\r\nConnection: Upgrade\r\nSec-WebSocket-Accept: "+token + "\r\n\r\n"
        self.connection.send(response.encode("utf-8"))
        while True:
            try:
                data = self.connection.recv(1024)
            except socket.error:
                print("socket error")
                break;
            if not data:
                print("no data")
                break
            msg = data.decode("unicode_escape")
            self.connection.send(('Hello, %s!' % msg).encode('utf-8'))
        self.connection.close()
        print('Connection from  closed.')

    def parse_data(self, msg):
        v = ord(msg[1]) & 0x7f
        if v == 0x7e:
            p = 4
        elif v == 0x7f:
            p = 10
        else:
            p = 2
        mask = msg[p:p + 4]
        data = msg[p + 4:]
        return ''.join([chr(ord(v) ^ ord(mask[k % 4])) for k, v in enumerate(data)])

    def parse_headers(self, msg):
        headers = {}
        header, data = msg.split('\r\n\r\n', 1)
        #print("header == "+header)
        for line in header.split('\r\n')[1:]:
            key, value = line.split(': ', 1)
            print("key =="+key)
            headers[key] = value
        headers['data'] = data
        return headers

    def generate_token(self, msg):
        #print("generate msg === "+msg)
        sStr = msg + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        sha1 = hashlib.sha1()
        sha1.update(sStr.encode('utf-8'))
        print("sha1 === " + sha1.hexdigest())

        token = base64.b64encode(sha1.digest())
        return token.decode("utf-8")


# 服务端
class websocket_server(threading.Thread):
    def __init__(self, port):
        super(websocket_server, self).__init__()
        self.port = port

    def run(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('127.0.0.1', self.port))
        sock.listen(5)
        print('websocket server started!')
        while True:
            connection, address = sock.accept()
            try:
                username = "ID" + str(address[1])
                thread = websocket_thread(connection, username)
                thread.start()
                clients[username] = connection
            except socket.timeout:
                print('websocket connection timeout!')



if __name__ == '__main__':
    server = websocket_server(9999)
    server.start()