from kazoo.client import KazooClient

# 创建一个 ZooKeeper 客户端
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# 确保路径存在
zk.ensure_path("/my/favorite")

# 创建一个 znode，路径为 "/my/favorite/node"，数据为 "data"
# zk.create("/my/favorite/node", b"data")

# 创建一个临时的序列节点，这个节点的声明周期随 session 的结束而结束
zk.create("/my/favorite/sss", b"data", ephemeral=True, sequence=True)

# 获取节点数据
path = "/my/favorite/node"
data, stat = zk.get(path)
print("Path: %s, Version: %s, data: %s" % (path, stat.version, data.decode("utf-8")))

zk.stop()
zk.close()
