from selenium import webdriver
import trio  # async library that selenium uses


async def start_listening(listener):
    async for event in listener:
        print(event)


async def main():
    driver = webdriver.Chrome()
    async with driver.bidi_connection() as connection:
        session, devtools = connection.session, connection.devtools
        # await session.execute(devtools.fetch.enable())
        await session.execute(devtools.network.enable())
        # listener = session.listen(devtools.fetch.RequestPaused)
        listener = session.listen(devtools.network.ResponseReceived)

        async with trio.open_nursery() as nursery:
            nursery.start_soon(start_listening, listener)  # start_listening blocks, so we run it in another coroutine
            driver.get("https://whatismytimezone.com/")


if __name__ == '__main__':
    trio.run(main)
