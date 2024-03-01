class Laptop:
    def get_content(self, param):
        return "Get content from Laptop: " + param


class Desktop:
    def get_content(self, param):
        return "Get content from Desktop: " + param


def get_computer(cond: int):
    if cond == 1:
        return Desktop()
    elif cond == 2:
        return Laptop()
    else:
        raise Exception("Wrong cond...")


if __name__ == "__main__":
    cond = 1
    computer = get_computer(cond)
    # 运行时才知道有没有 get_content 方法
    # 需要注释来说明有没有 get_content 方法
    res = computer.get_content("https://abc.com/")
    print(res)
