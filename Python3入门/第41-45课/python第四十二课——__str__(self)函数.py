'''
4.__str__(self):

作用：

创建完对象，直接打印对象名/引用名我们得到的是对象的内存信息(十六进制的地址信息)，

这串数据我们程序员并不关心，我们更希望看到的是属性赋值以后的内容(属性赋值的检测)，

那么我们就可以认为显示的重写__str__函数，来实现属性内容的返回显示

【注意】：

此函数必须有返回值，而且return后只能接受字符串数据
'''

class Person:
    def __init__(self,name,age,address):
        self.name=name
        self.age=age
        self.address=address

    def details(self):
        print('名字：'+self.name + ',年龄：' + str(self.age) + ', 籍贯：'+self.address)

    #重写_str__函数
    def __str__(self):
        print('我是__str__函数...')
        # return '123'
        return '名字：'+self.name + ',年龄：' + str(self.age) + ', 籍贯：'+self.address

#实例化对象
p=Person('hank',24,'深圳')
# print(p)

# p.details()



'''
5.魔术方法/魔术函数：

定义在class中的__开始__结尾的方法，就是魔术方法；

特点：

它们都有固定执行的时机，而且都是系统自动调用；不需要我们程序员关心

举例：

__init__、__del__、__str__...

6.self关键字：

出现的位置：

在函数(一般函数、构造函数)的形参位置

作用：

1).那个对象调用函数，此函数的self记录了这个对象的内存地址

2).为哪个对象实例化做准备，构造函数的self就记录了这个正在被创建的对象的内存地址

总结：属性和函数都是属于类的成员
'''