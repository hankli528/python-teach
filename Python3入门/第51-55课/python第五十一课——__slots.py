#！/usr/bin/env python
# Author:Hank
'''
2.__slots__：

作用：限制对象随意的动态添加属性

举例：

class Demo:

__slots__ = ('name','age','height','weight')

#实例化Demo对象

d = Demo()

#动态为d添加属性

d.name = 'abc'

d.age = 12

#可以动态添加的属性为：('name','age','height','weight')

#而sex不再范围内，所以执行代码报错了 --> AttributeError

# d.sex = '男'

print(d.name,d.age)

# print(d.sex)
'''

'''
演示__slots__属性的使用：
'''
class Person:
    __slots__ = ('name','age','height','weight')
    pass

#实例化Person对象
p=Person()

#动态为对象添加属性
# p.name='tom'
# p.age=18
# print(p.name,p.age)


'''
以下代码有问题:AttributeError...
'''
# print(p.__dict__)


'''
尝试为p对象动态添加sex属性，但是sex并不是_slots_元组对象范围内的内容，
所以不被允许，报错：AttributeErro
'''

# p.sex='男'
# print(p.sex)

# p.height=180.0
# print(p.height)

