import os
import socket
import threading

sock_type = "file"  # file/net

if sock_type == "net":
    # 通过系统调 socket：socket -> bind -> listen
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9000))
    server.listen()
    print("Server started on...")
elif sock_type == "file":
    """
    【1. Unix 域套接字概述】
    Unix 域套接字（Unix Domain Socket）是一种进程间通信（Inter-Process Communication, IPC）的方式，
    主要用于同一台服务器上的不同进程之间的通信。相较于其他 IPC 方式如管道、消息队列等，Unix 域套接字具有更高的性能和更广泛的应用场景。
    【2. Unix 域套接字的原理】
    Unix 域套接字的原理是基于文件描述符（File Descriptor）的，每个进程都拥有一个唯一的文件描述符，
    用于标识一个打开的文件或者套接字。Unix 域套接字实际上是一个特殊的文件，可以通过文件描述符进行操作。
    """
    # 确保socket文件不存在，防止 bind 时出错
    socket_file = '/tmp/unix_socket.sock'
    try:
        os.unlink(socket_file)
    except OSError:
        if os.path.exists(socket_file):
            raise

    # 创建一个Unix域套接字
    server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    server.bind(socket_file)  # 绑定到一个路径
    server.listen()
    print("Server started on...")
else:
    raise Exception("Err socket type not supported")


def cli_sock_handler(cli_sock, addr):
    while True:
        data = cli_sock.recv(1024)
        print(addr, data.decode('utf-8'))
        re_data = input()
        cli_sock.send(re_data.encode('utf-8'))


while True:
    cli_sock, addr = server.accept()
    # 用线程去处理新接收的链接
    client_thread = threading.Thread(target=cli_sock_handler, args=(cli_sock, addr))
    client_thread.start()
