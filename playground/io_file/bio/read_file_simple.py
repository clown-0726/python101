# 等执行读取操作的时候，程序处于阻塞状态
with open("abc.txt", "r") as f:
    lines = f.readlines()
    for line in lines:
        print(line)
