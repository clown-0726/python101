import asyncio
import time


# 定义一个同步函数
def sync_func():
    time.sleep(1)  # 模拟阻塞操作
    return "Hello World!"


# 定义一个异步函数
async def main():
    loop = asyncio.get_running_loop()
    result = await loop.run_in_executor(None, sync_func)  # 在另一个线程中运行同步函数
    print(result)


# 在同步代码中运行协程
asyncio.run(main())
