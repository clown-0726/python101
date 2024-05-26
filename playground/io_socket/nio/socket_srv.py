import socket
import time

# 通过系统调用 socket：socket -> bind -> listen
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)  # 设置为非阻塞
server.bind(('127.0.0.1', 9000))
server.listen()
print("Server started on...")

cli_sock_list = []
while True:
    try:
        cli_sock, addr = server.accept()

        cli_sock.setblocking(False)  # 设置为非阻塞
        cli_sock_list.append(cli_sock)
    except BlockingIOError as be:
        print("null...")
        time.sleep(1)

    # 遍历所有的 client socket 并返回数据
    for cli_sock_item in cli_sock_list:
        try:
            data = cli_sock_item.recv(1024)
            print(data.decode('utf-8'))
            cli_sock_item.send("Well done!".encode('utf-8'))
        except BlockingIOError as be:
            pass
