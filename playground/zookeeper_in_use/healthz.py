from kazoo.client import KazooClient
from kazoo.exceptions import KazooException


def check_zookeeper_with_kazoo(host: str, port: int = 2181):
    zk = KazooClient(hosts=f"{host}:{port}")
    try:
        zk.start(timeout=5)
        print(f"ZooKeeper at {host}:{port} is OK.")
        zk.stop()
        return True
    except KazooException as e:
        print(f"ZooKeeper at {host}:{port} is DOWN: {e}")
        return False
    except Exception as e:
        print(f"ZooKeeper at {host}:{port} is DOWN: {e}")


if __name__ == '__main__':
    check_zookeeper_with_kazoo(host='127.0.0.1')
