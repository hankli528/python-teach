#！/usr/bin/env python
# Author:Hank
'''
演示else语句和异常处理机制结合使用
'''
try:
    print('try...')
    print(10/0)
except:
    print('except...')
else:
    print('else...')
finally:
    print('finally...')