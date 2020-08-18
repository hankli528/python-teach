'''
3.析构函数

格式：__del__(self):

作用：

在程序结束前将对象回收，释放资源的行为
'''

'''
演示析构函数的使用：
'''

class Animal:
    #定义构造函数
    def __init__(self,name):
        print('我是构造函数...')
        self.name=name

    #定义析构函数
    def __del__(self):
        print('我是析构函数...')

    def func(self):
        a=Animal('如花')
        print(a)


#实例化Animal对象
a1=Animal('旺财')
# print(a1)

a2=Animal('来福')
# print(a2)

a2.func()