import asyncio


async def get_html():
    print("Waiting...")
    await asyncio.sleep(3)
    print("Done after {}s".format(3))


task1 = get_html()
task2 = get_html()
task3 = get_html()
tasks = [task1, task2, task3]

loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:  # 当用户强制退出的时候，进行任务的取消
    all_tasks = asyncio.Task.all_tasks(loop=loop)
    for task in all_tasks:
        print(task.cancel())
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
