final_result = {}


def generator_actual(key):
    total = 0
    nums = []
    while True:
        x = yield
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


def generator_proxy(key):
    while True:
        final_result[key] = yield from generator_actual(key)
        print(key + " Finished!")


def main():
    data_sets = {
        "a": [2, 3, 4],
        "b": [1, 2, 4],
        "c": [7, 8, 9],
    }
    for key, data_set in data_sets.items():
        print(key)
        g = generator_proxy(key)
        g.send(None)  # 预激生成器

        for val in data_set:
            g.send(val)
        g.send(None)
    print("Final result: ", final_result)


main()
