async def as_coroutine():
    pass


print(type(as_coroutine()))  # <class 'coroutine'>

"""
@coroutine
def function():
    ...
    yield...
    ...


async function():
    ...
    await...
    ...

---
async 将函数定义为一个可以调度的协程对象
await 后面跟一个可等待对象，并让出 CPU 执行权限
"""
