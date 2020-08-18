#！/usr/bin/env python
# Author:Hank
'''
案例一：
从键盘读入一个年份，判断其是否是闰年
判断闰年的标准：
能够被400整数或者能够被4整除并且不能被100整除
'''
year=int(input('请输入年份:(年)'))

if (year%400==0) or (year%4==0) and (year%100!=0):
    print('是闰年')
else:
    print('是平年')
