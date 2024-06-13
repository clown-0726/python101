import random
import string
import time
from collections import deque
from coroutine_4_gen import coroutine, YieldLoop


@coroutine
def arithmetic_sequence_100():
    """计算等差数列
    """
    sum_total = 0
    for i in range(0, 100):
        sum_total += yield i
    print("sum = ", sum_total)


@coroutine
def arithmetic_sequence_1000():
    """计算等差数列
    """
    sum_total = 0
    for i in range(0, 1000):
        sum_total += yield i
    print("sum = ", sum_total)


YieldLoop.instance().add_coroutine(arithmetic_sequence_100())
YieldLoop.instance().add_coroutine(arithmetic_sequence_1000())
YieldLoop.instance().run_until_complete()


# 生产者-消费者模型
@coroutine
def producer(q):
    """生产者
    """
    while True:
        good = "".join(random.sample(string.ascii_letters + string.digits, 8))
        q.append(good)
        cnt = len(q)
        print("producer produce good. cnt =", cnt)
        if cnt > 0:
            yield


@coroutine
def consumer(q):
    """消费者
    """
    while True:
        while len(q) <= 0:
            print("q is empty.")
            yield
        good = q.popleft()
        print("consumer consum good = {}, cnt = {}".format(good, len(q)))
        time.sleep(1)


q = deque()
YieldLoop.instance().add_coroutine(producer(q))
YieldLoop.instance().add_coroutine(consumer(q))
YieldLoop.instance().run_until_complete()
