#！/usr/bin/env python
# Author:Hank

'''
案例一：

演示自定义函数的使用：
包含：
1).定义格式的掌握
2).函数的好处

自定义函数：实现打印矩形的操作
两个原则需要考虑：
1).有没有形参？
有，2个

2).有没有返回值？
没有。
'''

def printRet(a,b):
    for i in range(a):
        for j in range(b):
            print('*',end='')
        print()

#需求：打印5行5列的矩形
# for i in range(5):
#     for j in range(5):
#         print('*',end='')
#     print()
# printRet(5,5)