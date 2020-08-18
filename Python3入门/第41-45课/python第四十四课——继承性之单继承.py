'''
2.继承性

继承：

使用场景：

1).生活层面：。。。

2).计算机层面：

两部分组成，一部分我们称为父类(基类、超类、superclass)，另一部分我们称为子类(派生类、subclass)，

子类可以使用父类中的成员(使用权)

继承性的好处：

1).代码复用性变强

2).代码扩展性变强

3).代码维护性变好

4).代码阅读性变好

继承性弊端：

类和类之间是一种强耦合关系

继承的好处要远远多于弊端，所以我们还是要经常使用继承的(合理)，切记不能为了继承而继承

分析：

继承体系可以很庞大(呈现树状结构图)，

越往上层的类，感觉越模糊，越不清晰

越往下层的类，感觉越清晰，越具体

所以得出结论，在之后的开发过程中创建父类的可能性变低，子类实例化的可能性极高
'''

'''
演示单继承的结构和使用：
父类：Person
子类：Teacher
'''
class Person:
    def __init__(self,name,age):
        print('我是Person类的构造...')
        self.name=name
        self.age=age

    #吃和睡
    def eat(self):
        print('吃一个...')

    def sleep(self):
        print('睡一个...')


'''
代码：(Person),就让Teacher类和Person发生继承关系
Person:父类
Teacher:子类
'''
class Teacher(Person):
    def __init__(self,name,age,salary):
        print('我是Teacher类的构造...')
        self.salary=salary
        '''
        为了给父类Person中的name和age属性赋值，
        所以我们需要在子类构造函数中显示的调用父类构造来实现
        关键字：super
        '''
        super().__init__(name,age)
        # super(Teacher, self).__init__(name,age)
        # Person.__init__(self,name,age)

    #教书
    def teach(self):
        print('教书育人...')

#实例化子类对象-->Teacher对象
t=Teacher('hank',24,6000.0)

#调用父类的属性
# print(t.name,t.age)

#调用子类的属性
# print(t.salary)

#调用父类函数
# t.eat()
# t.sleep()


#调用子类的函数
# t.teach()

