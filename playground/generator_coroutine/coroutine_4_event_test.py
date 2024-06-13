from coroutine_4_event import EventLoop


class TCPServer:
    def __init__(self, loop):
        self.loop = loop
        self.listen_sock = self.loop.create_listen_socket()  # 得到 SocketWrapper
        self.loop.add_corontine(self.serve_forever())

    async def handle_client(self, sock):
        while True:
            data = sock.recv(1024)
            if not data:
                print("Client disconnected")
                break
            await sock.send(data.upper())

    async def serve_forever(self):
        while True:
            sock, addr = await self.listen_sock.accept()  # 得到 SocketWrapper
            print("Client connect addr = {}".format(addr))
            self.loop.add_corontine(self.handle_client(sock))


if __name__ == "__main__":
    loop = EventLoop.instance()
    server = TCPServer(loop)

    loop.run_forever()
