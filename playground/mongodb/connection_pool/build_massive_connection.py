import pymongo
from concurrent.futures import ThreadPoolExecutor, ALL_COMPLETED, wait

MONGO_URI = ""
MONGO_POOL_SIZE = 100

mongo_client = pymongo.MongoClient(MONGO_URI, maxPoolSize=MONGO_POOL_SIZE)

"""
创建大量连接，进行观测
"""


def create_mongo_connection():
    collect_remote = mongo_client['filing_reports']['helper_sedar_plus_company_info']
    data = collect_remote.find_one({"x_info_data.id": "stock_oslobors"})
    print(data)


print("Create thread pool...")
executor = ThreadPoolExecutor(100)

all_task = []
for _ in range(100000):
    all_task.append(executor.submit(create_mongo_connection))
wait(all_task, return_when=ALL_COMPLETED)

print("Finished....")

if mongo_client:
    mongo_client.close()

if __name__ == '__main__':
    pass
