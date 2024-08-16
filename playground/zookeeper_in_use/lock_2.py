import time
from kazoo.client import KazooClient

if __name__ == '__main__':
    # 创建一个 ZooKeeper 客户端
    zk = KazooClient(hosts='127.0.0.1:2181')
    zk.start()

    # 创建一个锁
    print("lock 1...")
    lock = zk.Lock("/my_lock4", "")

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

    zk.stop()
    zk.close()
