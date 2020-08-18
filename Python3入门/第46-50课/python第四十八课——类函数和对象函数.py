'''
5.类函数和对象函数

类函数：在定义函数的上面一行书写@classmethod，特点：没有self 有cls

对象函数：定义在class中的普通的def函数
'''


'''
演示类函数和对象函数的定义使用：

总结：

在对象函数中，既能够直接使用对象属性和对象函数，也能够使用类属性和类函数

定义类函数，需要在函数的上面追加@classmethod注解符号，这样它的参数位置就有一个cls关键字

表示类的意思，而原本我们看到的self就不再了

在类函数中，只能直接使用类属性和类函数，不能直接使用对象属性和对象函数；

如果我们想要使用对象的成员，那么可以先实例化对象(用cls来完成),然后就可以实现对象内容的调用了
'''
class Demo:
    #类属性
    a=100
    def __init__(self,b):
        #对象属性
        self.b=b

    #对象函数
    def func1(self):
        print('我是对象函数func1...')

    def func2(self):
        '''
        思考：

        对象函数中能不能调用类属性和对象属性？
        能；

        对象函数中能不能调用类函数和对象函数？
        '''
        print(self.a)
        print(self.b)
        self.func1()
        self.func3()

        @classmethod
        def func3(cls):
            print('我是类函数func3...')

        @classmethod
        def func4(cls):
            '''
            思考：
            类函数中能不能调用类属性和类函数？
            能；

            类函数中能不能调用对象属性和对象函数？
            不能；
            '''
            print(cls.a)
            cls.func3()

            print(cls.b)
            cls.func1()

            '''
            思考：能不能在类函数func4中去使用对象属性b和对象函数func1()呢？
            可以；只要有对象就能实现；
            先实例化对象-->cls(num)
            '''

            d=cls(998)
            print(d.b)
            d.func1()

#实例化对象
d=Demo(200)
d.func2()

#类名调用类函数
# Demo.func4()


