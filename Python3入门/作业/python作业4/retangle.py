#！/usr/bin/env python
# Author:Hank

'''
定义一个retangle类，定义两个函数，一个计算矩形周长，一个计算矩形的面积，
实例化retangle对象，调用函数看到效果
提示：面积：长度 * 宽度 周长：2 * 长度 + 2 * 宽度
'''

class retangle:
    #定义长和高
    def __init__(self,length,high):
        self.length=length
        self.high=high

    #定义面积
    def area(self):
        print('面积为： %s' %(self.length * self.length))

    #定义周长
    def perimeter(self):
        print('周长为: %s' %(2*(self.length+self.high)))

r=retangle(10,20)
r.area() #求面积
r.perimeter() #求周长
