#！/usr/bin/env python
# Author:Hank
from person import Person
from dog import Dog
from cat import Cat

'''
测试模块

演示多态的使用：
'''

#实例化人、狗、猫对象
p = Person()
d = Dog('旺旺')
# c = Cat('咪咪')

p.feedDog(d)
# p.feedCat(c)
# p.feedAnimal(d)
# p.feedAnimal(c)