#！/usr/bin/env python
# Author:Hank

'''
演示函数的定义和使用细节：
'''

#默认参数：
#在设计自定义函数的时候，就存在一个默认值，就算在调用的时候不显示的传入实参，也不会报错。
#会用默认值来代替参与后期的运算
def m1(name='张三',age=23):
    print(name,age)

# m1('李四')
# m1(18)

'''
一般参数：
定义函数的时候有几个参数，在调用函数的时候就需要显示的传递几个实参，
而且要保证位置不能传错，否则会造成数据内容的不合理
'''
def m2(name,age,sex):
    print(name,age,sex)
# m2('王五',22,'男')


#关键字参数：
def m3(name,age,sex):
    print(name,age,sex)
# m3(age=25,name="钱八",sex="女")



#可变参数：(重要)
'''
格式：

def 函数名(*args,**kwargs):

函数体

参数的讲解：

*args：可以接受0~无穷多个单值，将它们存入到一个元祖中使用

**kwargs：接可以受0~无穷多个键值对，将它们存入到一个字典中使用
'''
def m4(*args,**kwargs):
    print(args,type(args))
    print(kwargs,type(kwargs))

# m4()
# m4(10,2,2,3,4,True,'adc',name='hank')



'''
需求：实现整数求和功能？
'''
def my_sum(*args):
    #遍历args中的每一个元素，将他们累加起来
    mySum=0
    for i in args:
        mySum += i
    return mySum
mySum=my_sum(1,2,3,4,5)
print('和值为：%d' %mySum)