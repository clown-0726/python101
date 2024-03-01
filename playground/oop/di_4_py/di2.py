from functools import wraps


class ServiceInjector:
    def __init__(self):
        self.deps = {}

    def register(self, name=None):
        name = name

        def decorator(thing):
            """
            thing here can be class or function or anything really
            """

            if not name:
                if not hasattr(thing, "__name__"):
                    raise Exception("no name")
                thing_name = thing.__name__
            else:
                thing_name = name
            self.deps[thing_name] = thing
            return thing

        return decorator

    def inject(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            new_args = args + (self.deps,)
            return func(*new_args, **kwargs)

        return decorated


# -------------------------------------------------------
# usage:
si = ServiceInjector()


# use func.__name__, registering func
@si.register()
def foo(*args):
    return sum(args)


# we can rename what it's been registered as, here, the class is registered
# with name `UpperCase` instead of the class name `UpperCaseRepresentation`
@si.register(name="UpperCase")
class UpperCaseRepresentation:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value.upper()


# register float
si.register(name="PI")(3.141592653)


# -------------------------------------------------------

# inject into functions
@si.inject
def bar(a, b, c, _deps):  # the last one in *args would be receiving the dependencies
    UpperCase, PI, foo = _deps['UpperCase'], _deps['PI'], _deps['foo']
    print(UpperCase('abc'))  # ABC
    print(PI)  # 3.141592653
    print(foo(a, b, c, 4, 5))  # = 15


bar(1, 2, 3)


# inject into class methods
class Foo:
    @si.inject
    def my_method(self, a, b, _deps, kwarg1=30):
        return _deps['foo'](a, b, kwarg1)


print(Foo().my_method(1, 2, kwarg1=50))  # = 53
