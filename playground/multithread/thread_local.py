import threading

"""
threading.local 函数可以创建线程本地数据空间，其下属性对每个线程独立存在。
"""

l = threading.local()

# 在主线程中声明一个值
l.x = 1


# 在其他线程运行会报错
def f():
    l.x = 5
    print(l.x)


threading.Thread(target=f).start()

# 在当前线程运行，是可以成功得到 x 的值
print(l.x)
