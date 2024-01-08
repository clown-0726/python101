from collections import ChainMap

user_dict1 = {'a': 'zhangsan', 'b': 'lisi1'}
user_dict2 = {'b': 'lisi2', 'c': 'wangwu'}

# 组合成新的 dict
new_dict = ChainMap(user_dict1, user_dict2)
# 可以对组合后的 dict 添加新的对象
new_dict.new_child({'d': 'zhaoliu'})
# 组合后的 dict 不是新的 dict 对象，而是对原有数组的引用
print(new_dict.maps)
# 最终遍历数据
for key, item in new_dict.items():
    print(key, item)

'''
ChainMap 提供了一种更简便的方式遍历所有 dict 数据的方式
组合后的 dict 不是新的 dict 对象，而是对原有数组的引用
如果遍历操作中有重复值，那么会默认用第一个
'''
