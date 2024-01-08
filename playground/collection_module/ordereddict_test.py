from collections import OrderedDict

user_dict = OrderedDict()
user_dict['b'] = 'zhangsan'
user_dict['c'] = 'lisi'
user_dict['a'] = 'wangwu'
print(user_dict)

# OrderedDict 比 Dict 独有的方法，移除最后一个
user_dict.popitem()
print(user_dict)

# OrderedDict 比 Dict 独有的方法，移动到最后一个
user_dict.move_to_end('b')
print(user_dict)


'''
python2 dict 是无序的，但是 python3 dict 和 OrderedDict 都是有序的
OrderedDict 是 dict 子类，是对 dict 的增强
'''
