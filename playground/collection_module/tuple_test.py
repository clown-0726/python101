# tuple 的拆包
name_tuple = ('zhangsan', 'M', 28)
# 将内容进行拆包
name, gender, age = name_tuple
# 只拆出需要的数据，其他数据放在 *other 中
name2, *other = name_tuple
print(name, gender, age)
print(name2, other)

# 作为 dict 的 key
tuple_dict = {}
tuple_dict[name_tuple] = 'zhangsan'
print([name_tuple])

'''
immutable 的重要性：
1. 性能优化：元素全部为 immutable 的 tuple 会作为常量在编译时确定，因此产生显著的速度差异
2. 线程安全
3. 可以作为 dict 的 key。可 hash 对象可以作为 dict 的 key，这也是 tuple 重要的特征。
4. 拆包特性
'''
