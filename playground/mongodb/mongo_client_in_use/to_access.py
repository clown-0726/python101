from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED, wait
import importlib
import sys


def try_to_import():
    if 'util_4_mongo_client' in sys.modules:
        importlib.reload(sys.modules['util_4_mongo_client'])
    import util_4_mongo_client

    print(id(util_4_mongo_client.get_mongo_client()))


print("Create thread pool...")
executor = ThreadPoolExecutor(3)

all_task = []
for _ in range(10):
    all_task.append(executor.submit(try_to_import))
wait(all_task, return_when=ALL_COMPLETED)

print("Finished....")

"""
Create thread pool...
I am sleeping...
140586407161328140586407161328

140586407161328
140586407161328
140586407161328
140586407161328
140586407161328
140586407161328
I am sleeping...
140586473695120
140586473695120
Finished....

---------
上面结果出现的原因：
一开始的几个线程都没有 util_4_mongo_client 模块，都会阻塞在 import util_4_mongo_client
等到有一个完成 import，其余的都继续往下执行，因此会出现多个一致 id 的 MongoClient 对象

只有再进入执行方法的同理
"""

if __name__ == "__main__":
    pass
