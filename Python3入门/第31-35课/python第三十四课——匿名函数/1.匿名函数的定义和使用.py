#！/usr/bin/env python
# Author:Hank
'''
演示匿名函数的定义和使用
'''
#定义无参有返回值的有名函数：
def func():
    return True

#定义无参有返回值的匿名函数
f=lambda : True

#调用有名函数执行
print(func())

#调用匿名函数执行
print(f())

print('*'*50)


#定义无参无返回值的有名函数：
def func():
    print(True)

#定义无参无返回值的匿名函数：
f=lambda : print(True)

#调用有名函数执行
func()

#调用匿名函数执行
f()


'''
需求：字符串数据'This is \n a \ttest' --> 得到'This is a test'
步骤一：使用字符串的split()函数-->作用：可以默认去除字符串中的空格、\n、\t等内容
        然后将字符串数据以列表的形式返回

步骤二：使用字符串的join()函数-->以空格作为连接的格式，将列表中的元素连接成为一个字符串数据返回
'''
str1='this is \na \ttest'
lt=str1.split()

str2=' '.join(lt)
print(str1,type(str1))
print(str2,type(str2))

print(lambda x:' '.join(x.split())(str1))


print('*'*50)

'''
分类匿名函数-->以参数
    1).1个参数
    2).多个参数
    3).默认参数
    4).可变参数
'''
#先定义有名函数
def m1(a):
    return a**2

def m2(a,b):
    return a+b

def m3(s2,s1='hello'):
    return s1+s2

print(m1(2))
print(m2(3,5))
print(m3('world','abc'))

print('*'*50)

print((lambda x:x**2)(2))
print((lambda x,y:x+y)(3,5))
print((lambda x,y='hello':y+x)('world'))

print('*'*50)

#定义匿名函数得到两个数中的较大值
my_max=lambda x,y:x if x>y else y

#调用匿名函数执行
print(my_max(10,20))

print('*'*50)

#演示有名函数和匿名函数嵌套的情况
def say(content):
    return (lambda x:x + '你好')(content)

print(say('李白'))