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
    def __init__(self, name):
        self.name = name


# class SingletonType(type):
#     _instance_lock = threading.Lock()
#
#     def __call__(cls, *args, **kwargs):
#         if not hasattr(cls, "_instance"):
#             with SingletonType._instance_lock:
#                 if not hasattr(cls, "_instance"):
#                     cls._instance = super(SingletonType, cls).__call__(cls, *args, **kwargs)
#         return cls._instance
#
#
# class S3ConnectionHandler(metaclass=SingletonType):
#     def __init__(self, name):
#         self.name = name


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
    s3connectionhandler1 = Foo(name='xiaoming')
    s3connectionhandler2 = Foo(name='xiaohua')
    print(s3connectionhandler1.name)
    print(s3connectionhandler2.name)

    print(s3connectionhandler1 is s3connectionhandler2)
