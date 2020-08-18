#！/usr/bin/env python
# Author:Hank

'''
对函数(模块中的)进行函数测试
定义两个需要被测试的函数：
'''
#求和函数
def mySum(x,y):
    return x+y

#相减函数
def mySub(x,y):
    return x-y

# print(mySum(10,20))


#导入测试模块 import unittest
import unittest
#导入需要被测试的函数
# from method import mySum
# from method import mySub

'''
对函数(模块中的)进行单元测试：
步骤一：
需要先导入测试模块unittest，然后自定义类继承unittest中的TestCase类，
并且去重写setUp()和tearDown()函数
步骤二：
将需要被测试的函数命名修饰一下(加上test_来定义)，
在函数体中通过self调用assertEqual()函数，目的：断言结果
步骤三：
启动测试模块
如果控制台显示红条，表示断言失败，可以认为测试的方法功能有问题
如果控制台显示绿条，表示断言成功，可以认为测试的方法功能ok
'''
#自定义类：
class MyTest(unittest.TestCase):
    '''
    以下代码发生子类重写父类函数的行为
    理解：setUp()和tearDown()函数的作用
    对于setUp()函数而言：
    在执行主模块的时候由系统自动调用(时机：在被测试的函数执行之前被调用执行)
    对于tearDown()函数而言：
    在执行主模块的时候由系统自动调用(时机：在被测试的函数执行之后被调用执行)
    '''
def setUp(self):
    print('对函数开始单元测试...')

def tearDown(self):
    print('单元测试结束了...')

'''
修饰需要被测试的函数
以下两个函数都是由系统自动调用(时机：分别在setUp()函数之后和tearDown函数之前)
'''

def test_mySum(self):
    '''
    断言：预言(测试)、就是推断这个函数执行以后的结果是什么？
    通过self调用assertEqual(,,)
    参数1：需要被测试的函数 【注意】此函数调用必须有小括号以及实参
    参数2：断言的结果
    参数3：如果断言失败了，错误提示信息
    '''
    self.assertEqual(mySum(2,1),3,'加法功能逻辑有误...')

def test_mySub(self):
    self.assertEqual(mySub(5,1),1,'减法功能逻辑有误...')

if __name__=='__main__':
    #需要通过测试模块unittest调用其main()
    unittest.main()