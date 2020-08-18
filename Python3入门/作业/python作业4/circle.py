#！/usr/bin/env python
# Author:Hank

'''
定义一个Circle类，定义一个计算面积的函数，实例化Circle对象，调用函数看到效果
提示：pi * r * r
'''

import math

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        print('圆面积为： %s' %(math.pi * self.radius**2))

c=Circle(1)
c.area()