import threading
import pymongo
import time

"""
当你首次导入一个模块时，Python 会执行该模块的所有代码。然后，Python 会将这个模块的名称和对应的模块对象存储在一个内部字典中（可以通过 sys.modules 访问）。
如果你再次尝试导入同一个模块，Python 会首先检查这个内部字典，看是否已经存在一个名为该模块名称的条目。如果存在，Python 就会直接返回对应的模块对象，而不会再次执行模块的代码。
"""

MONGO_URI = ""
MONGO_POOL_SIZE = 100

# 基于 Python 加载模块的机制，下面的加锁似乎是没有意义的？
_mongo_client = None
mongo_client_lock = threading.Lock()
with mongo_client_lock:
    print("I am sleeping...")
    time.sleep(3)
    if _mongo_client is None:
        _mongo_client = pymongo.MongoClient(MONGO_URI, maxPoolSize=MONGO_POOL_SIZE)


def get_mongo_client():
    return _mongo_client
