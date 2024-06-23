import asyncio
from asyncio import Lock
import aiohttp

# 这个锁和一般的线程锁不一样，这个锁是用户态标识位实现的
lock = Lock()

cache = {}


async def get_content(url):
    async with lock:
        if url in cache:
            return cache[url]

        async with aiohttp.ClientSession() as session:
            stuff = await session.request('GET', url)
            cache[url] = stuff
            return stuff


async def get_url_1(url):
    result = await get_content(url=url)
    html = await result.text()
    print(html)


async def get_url_2(url):
    result = await get_content(url=url)
    html = await result.text()
    print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [
        asyncio.ensure_future(get_url_1("https://www.baidu.com")),
        asyncio.ensure_future(get_url_2("https://www.baidu.com")),
    ]
    loop.run_until_complete(asyncio.wait(tasks))
