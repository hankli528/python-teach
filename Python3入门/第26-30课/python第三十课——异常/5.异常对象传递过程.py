#！/usr/bin/env python
# Author:Hank
'''
演示异常对象传递的过程（往上“抛”），并将其解决
'''
# def func1():
#     print('func1...')
#     print(10/0)
#
# def func2():
#     print('func2...')
#     try:
#         func1()
#     except Exception as e:
#         print(e)
#
# def func3():
#     print('func3...')
#     func2()
#
# try:
#     func3()
# except Exception as e:
#     print(e)
#
# print('我能执行吗？')


'''
需求：从键盘读入n个整数，得到正数、负数和零的个数，输入其他内容终止循环
'''
zs=0
fs=0
ling=0

while 1:
    try:
        num=int(input('请输入一个整数：'))
    except:
        break

    if num>0:
        zs+=1
    elif num<0:
        fs+=1
    else:
        ling+=1
print('正数的个数为：{}'.format(zs))
print('负数的个数为：{}'.format(fs))
print('零的个数为：{}'.format(ling))