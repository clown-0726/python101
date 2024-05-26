import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.baidu.com', 80))
s.sendall(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n")

buf_all = b""
while True:
    buf = s.recv(1024)
    if buf:
        buf_all += buf
    else:
        break

print(buf_all.decode("utf-8"))
