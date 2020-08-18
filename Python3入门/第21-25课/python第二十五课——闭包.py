#！/usr/bin/env python
# Author:Hank

'''
满足闭包的三个条件：

1).有外部函数和内部函数这样的结构

2).外部函数中定义的变量被内部函数所使用

3).内部函数对象作为返回值被外部函数返回
'''

#演示闭包的定义和使用：
# def outer():
#     a=10
#     def inner():
#         print(a+10)
#     return inner

# i=outer()
# i()
# print(i,type(i))


#强化闭包的使用：

#案例1：
def outer():
    # count=[0]
    count=0
    def inner():
        nonlocal  count
        # count[0]+=1
        count+=1
        print('hello,hank,%s haha'%count)
    return inner()

# i=outer()
# j=outer()
# print(id(i),id(j))


def outer():
    num1=10
    num2=20
    def inner(num3):
        print(num1+num3)
        print(num2+num3)
    return inner

# i=outer()
# i(100)
outer()(200)