#！/usr/bin/env python
# Author:Hank
'''
设计Car类，初始化属性speed，提供一个run函数
'''
import time
class Car:
    def __init__(self,speed):
        self.speed=speed

    #将Road对象传给run函数,绑定微弱的关联关系
    def run(self,road):
        #得到road的长度
        l=road.length

        #循环让汽车跑一会儿
        i=0
        while i<= 10:
            print('汽车正在水产路上飞速的行驶...')
            time.sleep(1)
            i+=1
            print('汽车行驶到目的地，一共花费：%s时间' %(l/self.speed))


'''
设计一个Road类，有属性length
'''
class Road:
   #定义构造函数：初始化length
    def __init__(self,length):
        self.length=length


'''
测试：
实例化Road,Car对象，然后调用函数，完成效果的显示
'''
r=Road(60)
c=Car(30)
c.run(r)