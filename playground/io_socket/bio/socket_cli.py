import socket

sock_type = "file"  # file/net

if sock_type == "net":
    cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli_sock.connect(('127.0.0.1', 9000))
elif sock_type == "file":
    print("xxx")
    socket_file = '/tmp/unix_socket.sock'
    # 创建Unix域套接字
    cli_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    cli_sock.connect(socket_file)
else:
    raise Exception("Err socket type not supported")

while True:
    re_data = input()
    cli_sock.send(re_data.encode('utf-8'))
    data = cli_sock.recv(1024)
    print(data.decode('utf-8'))
    # client.close()
