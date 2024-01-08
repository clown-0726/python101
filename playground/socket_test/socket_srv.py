import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8888))
server.listen()


def handle_sock(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf-8'))
        re_data = input()
        sock.send(re_data.encode('utf-8'))


while True:
    sock, addr = server.accept()
    # 用线程去处理新接收的链接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
