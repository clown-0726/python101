def g1(gen):
    yield from gen


def main():
    g = g1()
    g.send(None)


main()

# main 调用方 g1（委托生成器）gen 子生成器
# yield from 会在调用方与子生成器之间建立一个双向通道
