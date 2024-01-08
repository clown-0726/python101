'''
Counter 是 C 语言实现的，性能很高
Counter 一般用于统计可迭代对象的出现次数问题
Counter 也可以用于解决 top n 问题（堆数据结构实现）
'''

from collections import Counter

fruits = ['apple', 'orange', 'apple', 'banana', 'orange']
fruits_count = Counter(fruits)
# 也可以更新一下再做统计
fruits_count.update(['apple', 'banana'])
print(fruits_count)

# 统计 top 问题
topn_count = fruits_count.most_common(2)
print(topn_count)
