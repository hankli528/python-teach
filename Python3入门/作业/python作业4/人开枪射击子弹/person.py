#！/usr/bin/env python
# Author:Hank
'''
第三个：

设计一个人类：Person

1).初始化枪(构造来实现)

2).开火(fire) 装填(fillbullet)
'''
class Person:
    def __init__(self,gun):
        self.gun=gun

    #开火
    def fire(self):
        self.gun.shoot()

    #装填子弹
    def fillBullet(self,number):
        self.gun.bulletbox.bulletCount += number
        print('装填了%s发子弹，一共剩余： %s子弹' %(number,self.gun.bulletbox.bulletCount))
