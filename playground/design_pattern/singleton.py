import threading


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


class Foo(metaclass=SingletonType):
    pass
    # def __init__(self, name):
    #     self.name = name


class Other(Foo):
    def __init__(self, name):
        self.name = name


# class S3ConnectionHandler:
#     _instance_lock = threading.Lock()
#
#     def __init__(self, name):
#         self.name = name
#
#     def __new__(cls, *args, **kwargs):
#         if not hasattr(S3ConnectionHandler, "_instance"):
#             with S3ConnectionHandler._instance_lock:
#                 if not hasattr(S3ConnectionHandler, "_instance"):
#                     S3ConnectionHandler._instance = object.__new__(cls)
#         return S3ConnectionHandler._instance


if __name__ == '__main__':
    # foo1 = Foo(name='Xiaoming')
    # foo2 = Foo(name='Xiaohua')
    #
    # print(foo1.name)
    # print(foo2.name)
    # print(foo1 is foo2)

    other1 = Other(name='Xiaoming')
    other2 = Other(name='Xiaohua')
    print(other1.name)
    print(other2.name)
    print(other1 is other2)
