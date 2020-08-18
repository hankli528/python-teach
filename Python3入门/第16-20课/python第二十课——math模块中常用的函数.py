#！/usr/bin/env python
# Author:Hank
'''
属性：

e：自然数

pi：圆周率

函数：

ceil()：向上取整

floor()：向下取整

sqrt()：开平方根

radians()：角度转弧度

degrees()：弧度转角度
'''

import math

#属性:e和pi
# print(math.e)
# print(math.pi)


#函数：
#ceil(),floot():
# print(math.ceil(3.14))
# print(math.floor(3.14))
# print(math.ceil(-3.14))
# print(math.floor(-3.14))


#radians(),degrees()
# print(math.radians(180)) #3.141592653589793
# print(math.radians(360)) #6.283185307179586
# print(math.degrees(6.283185307179586))

'''
sys模块中的argv属性：
将当前正在被执行的这个.py文件的绝对路径(完整路径)-->str数据存入到列表对象中返回
'''
import sys
# print(sys.argv)

'''
os模块中的system()函数：

在参数位置接受一些dos指令，执行相应的操作...
'''

import os
# print(os.system('ipconfig'))
# print(os.system('dir'))
# print(os.system('cls'))

