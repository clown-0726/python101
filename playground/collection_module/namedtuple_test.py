from collections import namedtuple

'''
namedtuple 其实是动态执行 python 模版代码定义的 class 类。

适合于数据操作场景，比如从 DB 中取出的数据一般都是 tuple 类型，为了将其对象话，我们不需要定义一个单独的类，可以借助 namedtuple 将其映射为对象类型。
1. 代码简单，操作更加高效
2. 节省空间，省略了很多类内置的变量
'''
# 通过 namedtuple 快速声明一个 User 类
User = namedtuple('User', ['name', 'age', 'height', 'edu'])

# 通过 tuple 进行实例化赋值
user_tuple = ('zhangsan', 29, '180')
user = User(*user_tuple, 'master')

print(type(User))  # <class 'type'>
print(user.name, user.age, user.height, user.edu)

# 通过 dict 进行实例化赋值
user_dict = {
    'name': 'zhangsan',
    'age': 30,
    'height': '170',
}

user = User(**user_dict, edu='master')
print(type(User))  # <class 'type'>
print(user.name, user.age, user.height, user.edu)

# 同时具备 tuple 的拆包特性
name, age, *other = user
print(name, age, other)
