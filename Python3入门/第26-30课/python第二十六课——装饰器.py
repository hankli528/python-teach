#！/usr/bin/env python
# Author:Hank
'''
装饰器是闭包的一种使用场景；

python中的装饰器在定义上需要传入一个函数对象，

在此函数执行之前或者之后都可以追加其它的操作，

这样做的好处是，在不改变源码(原本业务逻辑的)同时，进行功能的扩展；

它在python中一般被使用在，性能测试，插入日志，事务管理，权限校验...

它就好比是一个切面(可插拔的)，也就是我们之后学习中会提到的叫面向切面编程(aop)

开放封闭原则：

开放：

在不改动源码(破坏原本业务逻辑)的同时扩展新的功能

封闭：

不允许随意去修改源代码
'''
import time
'''
说明装饰器的好处：
部门A：维护和管理数据信息平台

信息平台：内部封装了一些核心的api和接口

装饰器：函数(fn)

部门B：
    m1():
    func1()
    func2()
    func3()

部门C：
    func4()
    func5()
    func6()
'''

# def outer(fn):
#     def inner():
#         print('功能开始前记录日志...')
#         start=time.time()
#         fn()
#         print('功能介绍了记录日志...')
#         end=time.time()
#         print(end-start)
#     return inner
#
# @outer
# def test():
#     print('我是test函数...')
# test()


'''
演示函数装饰器的几种常见的定义格式：
'''
#无参数无返回值的装饰器
def outer(fn):
    def inner():
        print('功能开始前记录日志...')
        fn()
        print('功能介绍了记录日志...')
    return inner

@outer
def test():
    print('我是test函数...')
# test()


#无参有返回值的装饰器
def make_bold(fn):
    def wrapper():
        return '<b>' +fn()+'</b>'
    return wrapper

def make_italic(fn):
    def wrapper():
        return '<i>' +fn()+'</i>'
    return wrapper

@make_bold
@make_italic
def test():
    return 'hello zsq'
# print(test())


#有参有返回值的装饰器
def zhuangshiqi(fn):
    def wrapper(name,age,sex):
        print(name,age)
        fn(name,age,sex)
        print(sex)
        return 'abcdefg'
    return wrapper

@zhuangshiqi
def test(n,a,s):
    print('我叫： %s,年龄为：%s,性别是：%s' %(n,a,s))

# res=test(name='hank',age='22',sex='男')
# print(res)


#通用装饰器
def zsq(fn):
    def wrapper(*args,**kwargs):
        # print(args)
        fn(*args,**kwargs)
        # print(kwargs)
        # return '装饰器不难学'
    return wrapper

@zsq
def test(name,age,hobby):
    print('我叫：%s,年龄为： %s,爱好是： %s' %(name,age,hobby))

print(test(age='20',name='班长',hobby={'游戏':'魔兽','性别':'女','体育':'篮球'}))