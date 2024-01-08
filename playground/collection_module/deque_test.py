'''
deque 是线程安全的，list 是线程不安全的
Queue 的底层实现就是 deque，因此也是线程不安全的
deque 的操作方式和 list 很像
deque 是 C 语言实现的，性能很高
'''

from collections import deque

# 通过可迭代对象进行初始化
user_deque = deque([2, 5, 6, 2])

# 往队头/尾插入元素
user_deque.append(6)
user_deque.appendleft(9)

# 其他队列有的方法基本都有...

print(user_deque)
