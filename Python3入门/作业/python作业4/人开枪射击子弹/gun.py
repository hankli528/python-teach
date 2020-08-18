#！/usr/bin/env python
# Author:Hank
'''
第二个：

设计一个枪类：Gun

1).初始化子弹夹(构造来实现)

2).打(shoot) --> 判断是否还有子弹
'''
class Gun:
    #在初始化枪的同时将子弹夹准备好
    def __init__(self,bulletbox):
        self.bulletbox=bulletbox

    #打
    def shoot(self):
        #判断枪是否还有子弹
        if self.bulletbox.bulletCount == 0:
            print('没有子弹了...请装填弹药')
        else:
            self.bulletbox.bulletCount -= 1
            print('Boom...剩余%s发子弹' % self.bulletbox.bulletCount)

