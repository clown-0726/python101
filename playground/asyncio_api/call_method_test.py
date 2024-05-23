import asyncio
import time


def callback(sleep_time):
    time.sleep(sleep_time)
    print("Sleep time is " + str(sleep_time))


def stop_loop(loop):
    loop.stop()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    now = loop.time()  # 内部的时钟时间

    loop.call_soon(callback, 2)
    # loop.call_soon_threadsafe()
    loop.call_later(3, callback, 1)
    loop.call_at(now + 5, callback)
    # loop.call_soon(stop_loop, loop)
    loop.run_forever()
