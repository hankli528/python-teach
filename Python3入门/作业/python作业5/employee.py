#！/usr/bin/env python
# Author:Hank
'''
1).定义Employee类，属性：name、age、salary，功能：work

定义Manager和CommonEmployee类，都继承Employee类，

对于Manager类有自己独有的属性bonus，然后分别重写Employee中的work函数，

分别创建Manager和CommonEmployee对象，调用函数看效果
'''
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def work(self):
        pass
        # print('我正在工作...')

class Manager(Employee):
    def __init__(self,name,age,salary,bonus):
        self.bonus=bonus
        Employee.__init__(self,name,age,salary)
        print('姓名： %s,年龄： %s,工资 %s,奖金： %s' %(name,age,salary,bonus))

    def work(self):
        super().work()
        print('我正在给手下分配工作...')

class CommonEmployee(Employee):
    def __init__(self,name,age,salary):
        Employee.__init__(self,name,age,salary)
        print('姓名： %s,年龄： %s,工资： %s' % (name,age,salary))

    def work(self):
        print('我正在敲代码...')
        super().work()

m=Manager('张三',30,12000.0,5000.0)
m.work()
print(m.__dict__)

c=CommonEmployee('李四',23,6000)
c.work()
print(c.__dict__)