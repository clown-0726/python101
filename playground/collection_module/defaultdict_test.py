from collections import defaultdict

'''
用于针对集合数据生成 dict 统计或分类的场景。
提供更优雅高效的代码实现。
使用 C 语言实现，性能很高。
'''

'''
比如统计一个水果数组中水果的个数，结果为 dict
'''
# 原始的写法
# fruit_dict = {}
# fruits = ['apple', 'orange', 'apple', 'banana', 'orange']
#
# for item in fruits:
#     if item not in fruit_dict:
#         fruit_dict[item] = 0
#     else:
#         fruit_dict[item] += 1
#
# print(fruit_dict)


# 采用 dict 的 setdefault 对代码进行优化
# fruit_dict = {}
# fruits = ['apple', 'orange', 'apple', 'banana', 'orange']
#
# for item in fruits:
#     fruit_dict.setdefault(item, 0)  # 如果存在 key 则不会执行这个代码
#     if item not in fruit_dict:
#         fruit_dict[item] = 0
#     else:
#         fruit_dict[item] += 1
#
# print(fruit_dict)

# 最终采用 defaultdict 对代码进行优化
'''
defaultdict 接受一个可调用的类型，可以是基本类型，也可以是函数类型
由于最终的统计/分类结果都在一个 dict 中，
如果在运行过程中，在 dict 中找不到要操作的值，则使用传入的可调用类型
如果在运行过程中，在 dict 中找到了要操作的值，则使用找到的值
'''


# default_dict = defaultdict(int)
# fruits = ['apple', 'orange', 'apple', 'banana', 'orange']
# for item in fruits:
#     default_dict[item] += 1
#
# print(default_dict)

# 最终采用 defaultdict 对代码进行优化


def gen_default():
    return {
        'age': 0,
        'count': 0
    }


default_dict = defaultdict(gen_default)
fruits = [
    {'name': 'apple', 'age': 2}, {'name': 'orange', 'age': 1}, {'name': 'apple', 'age': 1},
    {'name': 'banana', 'age': 3}, {'name': 'orange', 'age': 1},
]
for item in fruits:
    default_dict[item['name']]['age'] += item['age']
    default_dict[item['name']]['count'] += 1

print(default_dict)
