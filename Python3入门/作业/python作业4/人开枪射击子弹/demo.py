#！/usr/bin/env python
# Author:Hank

'''
测试模块
'''
from bulletbox import BulletBox
from gun import Gun
from person import Person

#实例化：子弹夹、枪、人对象
bulletbox=BulletBox(5)
gun=Gun(bulletbox)
per=Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.fillBullet(10)
per.fire()
per.fillBullet(10)
per.fire()