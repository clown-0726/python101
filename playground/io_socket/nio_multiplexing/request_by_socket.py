import selectors
import socket

selector = selectors.DefaultSelector()


class RequestBySocket:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setblocking(False)
        self.buf_all = b""

    def connected(self, key):
        selector.unregister(key.fd)
        self.sock.sendall(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n")
        selector.register(self.sock.fileno(), selectors.EVENT_READ, self.receive)  # 只是注册，内核态并不会在可用时主动触发

    def receive(self, key):
        buf = self.sock.recv(1024)
        if buf:
            self.buf_all += buf
        else:
            selector.unregister(key.fd)
            print(self.buf_all.decode("utf-8"))

    def try_connect(self):
        try:
            self.sock.connect(('www.baidu.com', 80))
        except BlockingIOError:
            pass

        selector.register(self.sock.fileno(), selectors.EVENT_WRITE, self.connected)  # 只是注册，内核态并不会在可用时主动触发


def select_loop():
    # 主循环。不管是哪种多路复用技术，用户态需要不停的请求系统调用，询问准备好的 socket
    # 拿到准备好的 socket 后，主动调用注册的回调函数进行下一步处理
    while True:
        ready = selector.select()
        for key, mask in ready:
            callback = key.data
            callback(key)


if __name__ == '__main__':
    request_by_socket = RequestBySocket()
    request_by_socket.try_connect()

    select_loop()
