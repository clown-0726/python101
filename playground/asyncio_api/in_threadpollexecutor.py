import asyncio
from concurrent.futures import ThreadPoolExecutor

"""在 Event loop 中运行阻塞的方法
原理就是放在线程池中运行，性能是一样的
"""


def run_block_method(item: int):
    print(item)


loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor()
tasks = []
for item in range(10):
    task = loop.run_in_executor(executor, run_block_method, item)
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
