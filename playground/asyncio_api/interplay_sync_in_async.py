import asyncio


# 定义一个异步函数（协程）
async def hello_world():
    await asyncio.sleep(1)  # 模拟 I/O 操作
    print("Hello World!")


# 在同步代码中运行协程
asyncio.run(hello_world())

print("I am sync business code!")
