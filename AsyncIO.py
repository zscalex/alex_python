#子程序调用是通过栈实现的，一个线程就是执行一个子程序。
#子程序调用总是一个入口，一次返回，调用顺序是明确的。而协程的调用和子程序不同。
#协程看上去也是子程序，但执行过程中，在子程序内部可中断，然后转而执行别的子程序，在适当的时候再返回来接着执行。
#最大的优势就是协程极高的执行效率。因为子程序切换不是线程切换，而是由程序自身控制，因此，没有线程切换的开销，和多线程比，线程数量越多，协程的性能优势就越明显。
#第二大优势就是不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多。
#因为协程是一个线程执行，那怎么利用多核CPU呢？最简单的方法是多进程+协程，既充分利用多核，又充分发挥协程的高效率，可获得极高的性能。
#Python对协程的支持是通过generator实现的。

import time

def consumer():
    r = ''
    while True:#仅在收到信息时才执行此函数，如果此条件在一般函数中单独使用，则可能一直循环，但是在生成器函数中，只做接收信息的作用，相当于与另一函数建立连接
        n = yield r#n接收到的信息  r:返回值
        if not n:
            return print("x------------->")
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)#启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)#通过c.send(n)切换到consumer执行；consumer通过yield拿到消息，处理，又通过yield把结果传回；
        print('[PRODUCER] Consumer return: %s' % r)
        #ime.sleep(2)
    c.close()

c = consumer()
produce(c)


#asyncio是Python 3.4版本引入的标准库，直接内置了对异步IO的支持。
#asyncio的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO。
#yield from语法可以让我们方便地调用另一个generato
#当asyncio.sleep()返回时，线程就可以从yield from拿到返回值（此处是None），然后接着执行下一行语句。
#如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。

import asyncio

@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()#----------------?????
    while True:
        line = yield from reader.readline()#----------------??????
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))#--------------------??????
    # Ignore the body, close the socket
    writer.close()

loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]#任务列表
loop.run_until_complete(asyncio.wait(tasks))#循环执行coroutine
loop.close()#全部执行结束

#asyncio可以实现单线程并发IO操作。如果仅用在客户端，发挥的威力不大。如果把asyncio用在服务器端，例如Web服务器，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。

#asyncio实现了TCP、UDP、SSL等协议，aiohttp则是基于asyncio实现的HTTP框架

import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')#-----------------?????

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']#捕捉到请求的参数值
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop=loop)#不知道意义何在,有待解决-----------------------??????
    app.router.add_route('GET', '/', index)#服务器启动时，若有请求/的，返回index的输出页面 若是请请求/hello/任意名称 就会返回hello函数返回的页面
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)#loop.create_server()则利用asyncio创建TCP服务。
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()#消息循环
loop.run_until_complete(init(loop))
loop.run_forever()#------------------------------------???????

#-----------------------------------------------------------------
@asyncio.coroutine
def hello():
    print("Hello world!")
    r = yield from asyncio.sleep(1)
    print("Hello again!")

#===========两种等效，以下的为新的写法，比较简便易懂===================

async def hello():#表示其为生成器函数，且为异步IO使用的
    print("Hello world!")
    r = await asyncio.sleep(1)#await 时，可以进行先执行其他程序
    print("Hello again!")


async def test():
    print("test")
    await asyncio.sleep(1)
    print("test again")

test()
#-----------------------------------------------------------------