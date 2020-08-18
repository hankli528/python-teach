#！/usr/bin/env python
# Author:Hank
from myexception import MyException

'''
封装一个Person类
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.__age=age

    def setAge(self,age):
        #合法性校验
        if age<0 or age>130:
            raise MyException('年龄有误...')
        else:
            self.__age=age

    # def getAge(self):
    #     return self.__age

    def __str__(self):
        return 'name: %s, age:%s' %(self.name,self.__age)

#实例化对象
p=Person('李四',50)
# print(p)

p.setAge(150)
# print(p.setAge())