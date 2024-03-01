class ServiceFactory:
    def __init__(self):
        self.__services = {}

    def register(self, name, service_class):
        # Maybe add some validation
        self.__services[name] = service_class

    def create(self, name, *args, **kwargs):
        # Maybe add some error handling or fallbacks
        return self.__services[name](*args, **kwargs)


factory = ServiceFactory()


# ---------------------------------

class Service:
    def __init__(self):
        pass

    def create_post(self):
        print('I am create_post method!')


# 将 service 注册到工厂
factory.register('Service', Service)


# ---------------------------------

class Client:
    def __init__(self):
        pass

    def invoke(self):
        # 调用的时候不是直接 new 一个新的 Service 类的实例，而是通过工厂得到
        svc = factory.create('Service')
        svc.create_post()


if __name__ == '__main__':
    client = Client()
    client.invoke()
