#！/usr/bin/env python
# Author:Hank
'''
1.设计类
class 车：
 #属性
 颜色 = red
 品牌 = "BMW"
 车牌 = "沪A88888"
 #函数
 行驶():
 停止():
 2.实例化车对象
 car = 车()
 3.调用对象的属性或者函数完成需求
 print(car.颜色,car.品牌)
 car.行驶()
'''
#1.设计类
class Car(object):
    #属性
    color='red'
    brand='BMW'
    number='粤A888888'
    #函数
    def run(self):
        print('%s的%s,车牌为：%s,正在飞速行驶' %(self.color,self.brand,self.number))

    def stop(self):
        print('车停了...')

#2.创建对象
c1=Car()

#3.调用对象的属性或者函数完成需求
print(c1,type(c1),id(c1))
print(c1.color,c1.brand,c1.number)
c1.run()
c1.stop()

#再创建一个Car对象：c2
c2=Car()
print(c2,type(c2),id(c2))

#每个对象在类的成员(属性，函数)这块，都是彼此各自有一套
c2.run()
c2.stop()
c3=c1
print(c3,id(c3))
print(c1,id(c1))
c1.color='blue'
print(c3.color,c1.color)
print(c2.color)
c1=None

'''
请问：此时堆中有垃圾空间吗？
不是，原因：虽然c1失去了堆中对象的地址，但是c3中还记录着（它们指针连着呢）
'''

# print(c1.color)
# print(c3.color)