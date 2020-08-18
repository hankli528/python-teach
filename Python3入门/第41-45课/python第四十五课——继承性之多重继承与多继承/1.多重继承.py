'''
演示多重继承的结构和使用

子类：Dog

直接父类：Animal

间接父类：Creature
'''

#生物类
class Creature:
    def __init__(self,age):
        print('我是Creature类中的构造...')
        self.age=age

    def breath(self):
        print('吸一个...')

#动物类
class Animal(Creature):
    def __init__(self,age,name):
        print('我是Animal类中的构造...')
        self.name=name
        super().__init__(age)

    def eat(self):
        print('吃一个...')

#狗类
class Dog(Animal):
    def __init__(self,age,name,color):
        print('我是Dog类中的构造...')
        self.color=color
        super().__init__(age,name)

    def wang(self):
        print('汪汪叫...')

#实例化子类对象（Dog类）
d=Dog(3,'小宝','white')

#调用函数
d.wang()
d.eat()
d.breath()