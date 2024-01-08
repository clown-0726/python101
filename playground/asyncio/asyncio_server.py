import asyncio

"""
使用 asyncio 开发一个异步非阻塞的 http server
"""


class EchoServer:
    async def handle_client(self, reader, writer):
        while True:
            msg = await reader.read(1024)
            if not msg:
                print("Client disconnected")
                break
            print("recv msg: ", msg)
            writer.write(msg.upper())
            await writer.drain()

    async def serve_forever(self):
        server = await asyncio.start_server(self.handle_client, "127.0.0.1", "9999")

        addr = server.sockets[0].getsockname()
        print(f"Serving on {addr}")

        async with server:
            await server.serve_forever()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    echo_server = EchoServer()
    loop.run_until_complete(echo_server.serve_forever())
    """
    链接：
    telnet localhost 9999
    """
