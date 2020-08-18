#！/usr/bin/env python
# Author:Hank

'''
整理：4中最常见的自定义函数模型
1).无参无返回值
2).无参有返回值
3).有参无返回值
4).有参有返回值
'''
#定义无参无返回值自定义函数
def func1():
    print('hello method...')

#定义无参有返回值自定义函数
def func2():
    return True

#定义有参无返回值自定义函数
def func3(a,b):
    print(a+b)

#定义有参有返回值自定义函数
def func4(a,b):
    # func(a,b)
    return a if a>b else b
maxNum=func4(10,1000)
print('较大值为：'+str(maxNum))

func1()
func3(10,20)