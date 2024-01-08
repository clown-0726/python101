# yield from + iterable

my_list = [1, 2]
my_dict = {
    "a": 1,
    "b": 2,
}


def my_chain(*args, **kwargs):
    for my_iter in args:
        yield from my_iter


for value in my_chain(my_list, my_dict, range(7, 9)):
    print(value)


# -----------------

def g1():
    yield from range(999, 1001)


def main():
    g = g1()
    res1 = g.send(None)
    res2 = next(g)
    print(res1, res2)


main()
