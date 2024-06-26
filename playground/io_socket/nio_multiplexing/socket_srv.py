import select
import socket

srv_sock = socket.socket()
srv_sock.setblocking(False)
srv_sock.bind(("127.0.0.1", 9000))
srv_sock.listen()
print("Server started on...")

"""
这里的多路复用器可以选择 select poll epoll
如果要改成别的多路复用器，当前操作系统内核必须支持
比如要改成 epoll：
    select.poll()  -> select.epoll()
    select.POLLIN  -> select.EPOLLIN
    select.POLLOUT -> select.EPOLLOUT
"""
# 申请 epoll 对象并将这个对象的注册到内核的多路复用器中
selector = select.poll()
selector.register(srv_sock.fileno(), select.POLLIN)

connections = {}
contents = {}
while True:
    events = selector.poll(10)
    for fd, event in events:
        if fd == srv_sock.fileno():
            cli_sock, addr = srv_sock.accept()
            cli_sock.setblocking(False)
            print("New connection from {}".format(addr))
            selector.register(cli_sock.fileno(), select.POLLIN)
            connections[cli_sock.fileno()] = cli_sock
        elif event == select.POLLIN:
            cli_sock = connections[fd]
            content = cli_sock.recv(1024)
            if not content:
                selector.unregister(fd)
                cli_sock.close()
                connections.pop(fd)
            else:
                content = content.decode('utf-8').upper()
                # 改成关注写事件
                selector.modify(fd, select.POLLOUT)
                contents[fd] = content
        elif event == select.POLLOUT:
            cli_sock = connections[fd]
            try:
                content = contents[fd]
                cli_sock.send(content.encode('utf-8'))
                selector.modify(fd, select.POLLIN)
            except Exception as e:
                selector.unregister(fd)
                cli_sock.close()
                connections.pop(fd)
                contents.pop(fd)
