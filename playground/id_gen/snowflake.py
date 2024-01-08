import time
import threading

lock = threading.Lock()

"""
雪花算法（Snowflake）就如它的名字一样，即“世界上没有任何两片雪花是一样的。”
Snowflake 以 64 bit 来存储组成 ID 的4 个部分：
1、最高位占1 bit，值固定为 0，以保证生成的 ID 为正数；
2、中位占 41 bit，值为毫秒级时间戳；
3、中下位占 10 bit，值为工作机器的 ID，值的上限为 1024；
4、末位占 12 bit，值为当前毫秒内生成的不同 ID，值的上限为 4096；
"""


class Snowflake:
    # 定义Snowflake算法的各个参数
    def __init__(self, worker_id: int, datacenter_id: int, sequence: int = 0):
        # 开始时间截 (2015-01-01)
        self.twepoch = 1420041600000

        # 计算位数
        self._worker_id_bits = 5
        self._datacenter_id_bits = 5
        self._sequence_bits = 12

        # 计算最大ID
        self._max_worker_id = ~(-1 << self._worker_id_bits)  # 31
        self._max_datacenter_id = ~(-1 << self._datacenter_id_bits)  # 31
        self._max_sequence = ~(-1 << self._sequence_bits)  # 4095

        # 定义位偏移量
        self._worker_id_shift = self._sequence_bits  # 12 位
        self._datacenter_id_shift = self._sequence_bits + self._worker_id_bits  # 17 位
        self._timestamp_left_shift = self._sequence_bits + self._worker_id_bits + self._datacenter_id_bits  # 22 位

        # 初始化参数
        self.worker_id = worker_id
        self.datacenter_id = datacenter_id
        self.sequence = sequence
        self.last_timestamp = -1

    # 生成下一个唯一ID（线程安全的）
    def generate_id(self):
        with lock:
            # 获取当前时间戳
            timestamp = int(time.time() * 1000)

            # 如果当前时间小于上次生成ID的时间戳，则抛出异常
            if timestamp < self.last_timestamp:
                raise ValueError("Invalid system clock!")

            # 如果当前时间戳与上次时间戳相同，则自增序列号
            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & self._max_sequence
                # 如果序列号等于0，则需要进入下一毫秒重新生成ID
                if self.sequence == 0:
                    timestamp = self._wait_next_millis(self.last_timestamp)
            else:
                self.sequence = 0

            # 保存最后生成ID的时间戳
            self.last_timestamp = timestamp

            # 生成最终的唯一ID
            unique_id = ((timestamp - self.twepoch) << self._timestamp_left_shift) | \
                        (self.datacenter_id << self._datacenter_id_shift) | \
                        (self.worker_id << self._worker_id_shift) | \
                        self.sequence
            return unique_id

    # 阻塞到下一个毫秒，直到获得新的时间戳
    def _wait_next_millis(self, last_timestamp):
        timestamp = int(time.time() * 1000)
        while timestamp <= last_timestamp:
            timestamp = int(time.time() * 1000)
        return timestamp


# 测试方法
if __name__ == '__main__':
    snowflake = Snowflake(worker_id=1, datacenter_id=3)
    for _ in range(10):
        unique_id = snowflake.generate_id()
        # print(unique_id)
        print(bin(unique_id))
