import threading
import time
from kazoo.client import KazooClient

# 创建一个 ZooKeeper 客户端
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()


def working():
    # 创建一个锁
    print("lock 1...")
    lock = zk.Lock("/my_lock5", "")

    print("lock 2...")
    # 尝试获取锁
    if lock.acquire(blocking=True, timeout=None):
        try:
            print("lock 3...")
            time.sleep(10)
            # 在这里执行你的代码
            print("Got the lock.")
        finally:
            # 释放锁
            lock.release()


if __name__ == '__main__':
    thread1 = threading.Thread(target=working)
    thread2 = threading.Thread(target=working)
    thread3 = threading.Thread(target=working)
    thread4 = threading.Thread(target=working)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()

    zk.stop()
    zk.close()
