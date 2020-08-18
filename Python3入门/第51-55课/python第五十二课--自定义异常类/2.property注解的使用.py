#！/usr/bin/env python
# Author:Hank
from myexception import MyException
'''
4.@property和@属性名.setter注解的使用

作用：简化getter和setter函数，让你在使用过程中仿佛又回来了对象操作属性那般丝滑...

举例：

@property

def age(self):

return self.__age

@age.setter

def age(self,age):

self.__age = age

p.age = 50

print(p.age)

from myexception import MyException

'''

#@property注解的使用：
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def setAge(self,age):
        #合法性检验
        if age<0 or age>130:
            raise MyException('年龄有误...')
        else:
            self.__age=age

    def getAge(self):
        return self.__age

    @property
    def age(self):
        print('aaaaaaaaaa')
        return self.__age

    @age.setter
    def age(self,age):
        print('bbbbbbbbbbbb')
        #合法性校验
        self.__age=age

    def __str__(self):
        return 'name:%s,age:%s' %(self.name,self.__age)

#实例化对象
p=Person('lily',25)
print(p)

p.age=250
print(p.age)

p.setAge(100)
print(p.getAge())