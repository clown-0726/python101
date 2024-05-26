import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setblocking(False)
try:
    s.connect(('www.baidu.com', 80))
except BlockingIOError as e:
    pass

while True:
    try:
        s.sendall(b"GET / HTTP/1.1\r\nHost: www.baidu.com\r\nConnection: close\r\n\r\n")
        break
    except OSError as e:
        pass

buf_all = b""
while True:
    try:
        buf = s.recv(1024)
    except BlockingIOError as e:
        continue

    if buf:
        buf_all += buf
    else:
        break

print(buf_all.decode("utf-8"))
