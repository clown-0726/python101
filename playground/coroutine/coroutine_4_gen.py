import functools
import inspect
from collections import deque


def coroutine(func):
    """执行程序的装饰器
    程序被装饰之后，就可以被 YieldLoop 程序调度器进行调度了

    生成器任务函数 -> 可以被调度器调取的生成器任务函数 -> 加入到调度器执行队列 -> 调度执行
                    - 持有调取器实例
                    - 适配生成器任务函数
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        # 判断 gen 是不是生成器
        if inspect.isgenerator(gen):
            return CoroutineWrapper(YieldLoop.instance(), gen)
        else:
            raise RuntimeError(f"[Coroutine Wrapper] error. type({type(gen)}) is not supported.")

    return wrapper


# --------------------

class CoroutineWrapper:
    """生成器的协程适配器
    重写生成器方法：send、next
    使得生成器可以在调度器中执行
    """

    def __init__(self, loop, gen):
        # Yield loop 调度器
        self.loop = loop
        # 生成器计算函数
        self.gen = gen
        # 生成器计算函数的上下文
        self.context = None

    def send(self, val):
        """重写生成器的 send 方法
        """
        val = self.gen.send(val)
        self.context = val
        self.loop.add_runnables(self)

    def throw(self, tp, *rest):
        return self.gen.throw(tp, *rest)

    def close(self):
        return self.gen.close()

    def __next__(self):
        val = next(self.gen)
        self.context = val
        self.loop.add_runnables(self)

    def __getattr__(self, item):
        return getattr(self.gen, item)

    def __str__(self):
        return "coroutine wrapper : {}, context: {}".format(self.gen, self.context)


class YieldLoop:
    """程序调度器
    主要功能是从调度队列中取出一个任务并执行
    调度一次之后再放回执行队列中
    """
    current = None
    runnables = deque()

    @classmethod
    def instance(cls):
        if not YieldLoop.current:
            YieldLoop.current = YieldLoop()
        return YieldLoop.current

    def add_coroutine(self, coro):
        # 对类型进行判断
        assert isinstance(coro, CoroutineWrapper), "isinstance(coro) != CoroutineWrapper"
        self.add_runnables(coro)

    def add_runnables(self, coro):
        self.runnables.append(coro)

    def run_coroutine(self, coro):
        """执行协程
        """
        try:
            coro.send(coro.context)
        except StopIteration as e:
            print("coroutine {} stop.".format(coro))

    def run_until_complete(self):
        while YieldLoop.runnables:
            coro = YieldLoop.runnables.popleft()
            self.run_coroutine(coro)
