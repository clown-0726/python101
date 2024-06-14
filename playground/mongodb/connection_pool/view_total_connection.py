import time
import pymongo

print('Remote connection')
MONGO_URI = ""
conn_remote = pymongo.MongoClient(MONGO_URI, maxPoolSize=100)

"""
用于不断的监控当前连接的个数
"""

if __name__ == '__main__':
    db = conn_remote.admin
    while True:
        serverStatus = db.command('serverStatus')
        connections = serverStatus["connections"]
        print(f"current: {connections['current']}")
        print(f"available: {connections['available']}")
        print(f"totalCreated: {connections['totalCreated']}")
        # print(f"active: {connections['active']}")
        # print(f"threaded: {connections['threaded']}")
        # print(f"limitExempt: {connections['limitExempt']}")
        # print(f"exhaustIsMaster: {connections['exhaustIsMaster']}")
        # print(f"exhaustHello: {connections['exhaustHello']}")
        # print(f"awaitingTopologyChanges: {connections['awaitingTopologyChanges']}")
        print("---------------------------------")
        time.sleep(1)
