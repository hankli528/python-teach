class Person:
    def __init__(self,*args,**kwargs):
        print('我是Person类的构造...')
        # self.name=name
        # self.age=age
        self.args=args
        self.kwargs=kwargs

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