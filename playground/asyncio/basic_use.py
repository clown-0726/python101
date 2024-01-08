"""
Python3.4 之后提供的标准协程库
提供丰富的协程接口
"""

import asyncio
from functools import partial


async def get_html(url):
    print("Start getting url...")
    await asyncio.sleep(2)
    return "URL RESULT"


def callback(cb_str, future):
    print(cb_str)


# 得到事件循环器
loop = asyncio.get_event_loop()

# ------ 定义 task 任务
# 可以使用 asyncio.ensure_future 定义
# 也可以使用 loop.create_task 定义
# asyncio.ensure_future 底层调用了 loop.create_task 方法
task = asyncio.ensure_future(get_html("https://abc.com"), loop=loop)
# task = loop.create_task(get_html("https://abc.com"))
# 使用偏函数封装参数传递
task.add_done_callback(partial(callback, "I am back"))

loop.run_until_complete(task)
print(task.result())

# ------ 定义任务组
# gather: 比 wait 更高的功能抽象，可以对任务进行分组，也可以取消某个组的任务执行
tasks = [get_html(f"https://{i}.com") for i in range(10)]
# loop.run_until_complete(asyncio.wait(tasks))
loop.run_until_complete(asyncio.gather(*tasks))
