#！/usr/bin/env python
# Author:Hank
'''
定义几何图形类(GeometricObject)，定义一个计算面积的函数(getArea())
定义圆类和矩形类，都继承几何图形类，分别重写计算面积的函数
创建子类对象，调用函数，看效果
'''

import math

class GeometricObject:
    def getArea(self):
        pass

#求圆类面积
class Circle(GeometricObject):
    def __init__(self,radius):
        self.radius=radius

    def getArea(self):
        area=math.pi*(self.radius**2)
        print('圆面积为： %s' %area)

#求矩形类面积
class Retangle(GeometricObject):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def getArea(self):
        area=self.length*self.width
        print('矩形面积为： %s' % area)

c=Circle(10)
print(c.__dict__)
c.getArea()

print('*********************************')

r=Retangle(10,20)
print(r.__dict__)
r.getArea()