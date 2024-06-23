import asyncio


async def add(x, y):
    print("add...")
    await asyncio.sleep(1)
    return x + y


async def extract():
    print("extract...")


async def combine():
    """nested coroutine"""
    result = await add(1, 2)
    print("combine...", result)
    await extract()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    tasks = [combine(), extract(), add(2, 3)]
    loop.run_until_complete(asyncio.wait(tasks))
    print("I am finished!")
    loop.close()

'''
同理考虑 JavaScript，Python 中需要显示的指定一个 Event Loop，但是 JavaScript 的本质就会带有一个

当你在 async 函数内部使用 await 关键字时，它会立即返回一个 Promise，这会导致 JavaScript 运行时暂停执行 async 函数的后续代码，
将控制权归还给事件循环，直到等待的 Promise 解决（resolve）或拒绝（reject）。一旦 Promise 解决或拒绝，事件循环会回到 async 函数，恢复执行其后续代码。

async 函数中的代码并不是立即被放入事件循环栈中执行的。只有当 await 关键字使函数暂停时，事件循环才会介入。
在 await 关键字后面的代码（即 async 函数的剩余部分）会被包装成一个回调函数，并在 Promise 解决或拒绝时由事件循环调度执行。
'''
