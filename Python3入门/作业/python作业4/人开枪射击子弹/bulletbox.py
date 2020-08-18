#！/usr/bin/env python
# Author:Hank

'''
实现人开枪射击子弹
定义3个模块

第一个：

设计一个子弹夹类：BulletBox
'''

class BulletBox:
    #初始化子弹数
    def __init__(self,bulletCount):
        self.bulletCount=bulletCount
