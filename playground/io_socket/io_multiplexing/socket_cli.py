import socket

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_sock.connect(('127.0.0.1', 9001))

while True:
    re_data = input()
    cli_sock.send(re_data.encode('utf-8'))
    data = cli_sock.recv(1024)
    print(data.decode('utf-8'))
    # client.close()
