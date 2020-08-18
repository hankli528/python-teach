#！/usr/bin/env python
# Author:Hank

'''
实现自定义异常类：
'''
class MyException(Exception):
    def __init__(self,msg):
        super().__init__(msg)
