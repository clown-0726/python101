import time
import asyncio
from concurrent.futures import ThreadPoolExecutor

'''
Python 3.4及以上版本的asyncio模块提供了异步I/O支持。
然而，对于文件I/O，asyncio并没有直接提供异步操作的接口，因为在大多数操作系统中，文件I/O通常是阻塞的，不支持异步操作。
但你可以使用线程池来在后台执行文件I/O操作，这样主线程就可以在等待文件I/O操作完成的同时，执行其他任务。

在这个例子中，使用ThreadPoolExecutor创建了一个线程池，然后使用asyncio的run_in_executor方法在线程池中执行文件读取操作。
这样主线程就可以在等待文件读取完成的同时，执行其他任务，达到了异步的效果。
'''


def read_file(filename):
    with open(filename, 'r') as f:
        time.sleep(1)
        return f.read()


async def read_file_async():
    # 创建一个线程池
    with ThreadPoolExecutor() as executor:
        loop = asyncio.get_event_loop()
        # 在线程池中执行文件读取操作
        content = await loop.run_in_executor(executor, read_file, 'abc.txt')
        print(content)


async def main():
    # 创建一个异步任务
    task1 = asyncio.create_task(read_file_async())
    print("Test async...")
    # 等待所有任务完成
    await asyncio.gather(task1)


if __name__ == '__main__':
    asyncio.run(main())
