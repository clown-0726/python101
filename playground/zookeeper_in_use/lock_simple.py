import threading
from kazoo.client import KazooClient
from kazoo.recipe.lock import Lock
import time

# 连接到Zookeeper
zk = KazooClient(hosts='127.0.0.1:2181/insight')
zk.start()


def working():
    # 获取一个分布式锁
    lock = Lock(zk, "/my_lock7")

    with lock:
        # 在这个区块内的代码将获得锁执行
        print("Lock acquired")
        time.sleep(10)  # 模拟长时间处理任务

    print("Lock released")


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

# 关闭Zookeeper客户端
zk.stop()
zk.close()

'''
[zk: localhost:2181(CONNECTED) 4] ls /insight/my_lock7
[398361f44a6d4bf9a028a793fc4e2242__lock__0000000002, 6d1166b6bdbc4a49845acbb9226d8d0b__lock__0000000003, a3cd583438ec40df843ce6340ed1303e__lock__0000000004, d400b0d617e04ebd8a17d43e3268c5cb__lock__0000000005]
'''
