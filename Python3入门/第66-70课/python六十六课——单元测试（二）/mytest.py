#！/usr/bin/env python
# Author:Hank

import unittest
from person import Person

'''
对类(类中函数)进行单元测试：
可以测试类中所有的功能，所有步骤和之前函数的单元测试保持一致，
但是在调用assertEqual()函数之前必须先实例化一个当前类的对象
'''
class MyTest(unittest.TestCase):
    #子类重写父类中的函数：
    def setUp(self):
        print('对类开始单元测试...')

    def tearDown(self):
        print('对类单元测试结束了...')

    #测试函数：初始化函数
    def test_init(self):
        #实例化对象：Person对象
        p=Person('张三',25)
        #断言操作：assertEqual()方法被调用
        self.assertEqual(p.name,'张三','构造方法赋值操作有误...')

    def test_getAge(self):
        #实例化对象：Person对象
        p=Person('李四',15)
        self.assertEqual(p.getAge(),16,'获取年龄功能有误...')

#启动模块，开始测试
if __name__=='__main__':
    unittest.main()