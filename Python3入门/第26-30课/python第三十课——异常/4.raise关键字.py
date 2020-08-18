#！/usr/bin/env python
# Author:Hank
'''
演示：
    1.手动抛出异常对象-->raise关键字
    2.try-except代码不能解决语法错误
'''
try:
    print('try...')
    raise TypeError('类型有误的异常')
except TypeError as e:
    print(e)
else:
    print('else...')
finally:
    print('finally...')

try:
    # for=100
    pass
except:
    print('错了，错了')