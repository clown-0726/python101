import select
import socket
from collections import deque


class Future:
    """
    原理：相当于 Promise
    1. 协程对象的引用
    2. 完成标记
    3. 执行结果
    """

    def __init__(self, loop):
        self.done = False
        self.co = None
        self.loop = loop

    def set_coroutine(self, co):
        self.co = co

    def set_done(self):
        self.done = True

    # await <可等待对象>，会执行这个方法
    def __await__(self):
        if not self.done:
            # 让出 CPU
            yield self
        return


class SocketWrapper:
    def __init__(self, sock, loop):
        sock.setblocking(False)
        self.sock = sock
        self.loop = loop

    def fileno(self):
        return self.sock.fileno()

    def create_future_for_events(self, events):
        future = self.loop.create_future()

        def handler():
            future.set_done()
            self.loop.unregister_handler(self.fileno())
            if future.co:
                # 继续调度
                self.loop.add_coroutine(future.co)

        self.loop.register_handler(self.fileno(), events, handler)
        return future

    async def accept(self):
        while True:
            try:
                sock, addr = self.sock.accept()
                return SocketWrapper(sock=sock, loop=self.loop), addr
            except BlockingIOError:
                # 没有新的链接进来，则让出 CPU
                future = self.create_future_for_events(select.EPOLLIN)
                await future

    async def recv(self, backlog):
        while True:
            try:
                return self.sock.recv(backlog)
            except BlockingIOError:
                future = self.create_future_for_events(select.EPOLLIN)
                await future

    async def send(self, data):
        try:
            return self.sock.send(data)
        except BlockingIOError:
            future = self.create_future_for_events(select.EPOLLOUT)
            await future


class EventLoop:
    current = None
    runnables = deque()
    epoll = select.epoll()
    handlers = {}

    @classmethod
    def instance(cls):
        """保证 loop 是单例模式"""
        if not EventLoop.current:
            EventLoop.current = EventLoop()
        return EventLoop.current

    def create_future(self):
        return Future(loop=self)

    def create_listen_socket(self, ip="localhost", port=9999):
        sock = socket.socket()
        # 可以重用地址
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((ip, port))
        sock.listen()
        return SocketWrapper(sock=sock, loop=self)

    def register_handler(self, fileno, events, handler):
        self.handlers[fileno] = handler
        self.epoll.register(fileno, events)

    def unregister_handler(self, fileno):
        self.epoll.unregister(fileno)
        self.handlers.pop(fileno)

    def run_coroutine(self, co):
        try:
            future = co.send(None)
            future.set_coroutine(co)
        except Exception as e:
            print("coroutine {} stopped".format(co.__name__))

    def run_forever(self):
        while True:
            while self.runnables:
                self.run_coroutine(co=self.runnables.popleft())

            events = self.epoll.poll(timeout=1)  # 一秒超时
            for fileno, event in events:
                # 得到回调函数并执行
                handler = self.handlers.get(fileno)
                handler()

    def add_coroutine(self, co):
        self.runnables.append(co)
