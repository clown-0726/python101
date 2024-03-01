import hashlib
import uuid

MAX_WORKER_ID = 31  # 5-bit worker_id


def generate_worker_id(pod_name, namespace="default"):
    # 获取 Pod 的名称和命名空间
    # pod_name = os.environ.get('POD_NAME')
    # namespace = os.environ.get('POD_NAMESPACE')

    # 使用字符串哈希算法将名称和命名空间转换为数字
    hash_obj = hashlib.sha1()
    hash_obj.update(pod_name.encode('utf-8'))
    hash_obj.update(namespace.encode('utf-8'))
    hash_value = int(hash_obj.hexdigest(), 16)

    # 取模 MAX_WORKER_ID，确保 worker_id 的值在 0 到 MAX_WORKER_ID 范围内
    worker_id = hash_value % (MAX_WORKER_ID + 1)
    return worker_id


if __name__ == "__main__":
    worker_id_list = []
    for i in range(1, 31):
        # print(i)
        random_uuid = str(uuid.uuid4())
        print(random_uuid)
        worker_id = generate_worker_id(pod_name=random_uuid)
        # print(worker_id)
        worker_id_list.append(worker_id)

    print(worker_id_list)
    print(len(worker_id_list))
    print(len(set(worker_id_list)))
