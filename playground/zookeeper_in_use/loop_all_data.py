from kazoo.client import KazooClient


def print_all_znodes(zk, path):
    data, stat = zk.get(path)
    print("Path: [%s], Version: [%s], data: [%s]" % (path, stat.version, data.decode("utf-8")))
    children = zk.get_children(path)
    for child in children:
        print_all_znodes(zk, path + '/' + child)


# 创建一个 ZooKeeper 客户端
zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# 从根节点开始打印所有的 znode
print_all_znodes(zk, "")

zk.create("/myjaas", b"data", sequence=True)

zk.stop()
zk.close()

if __name__ == '__main__':
    pass
