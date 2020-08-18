#！/usr/bin/env python
# Author:Hank
'''
演示递归的弊端：
'''
def mySum(num):
    if num == 1:
        return 1
    return num+mySum(num-1)

mySum(998)

'''
【注意】：
递归可以解决绝大多数循环能干的事情，但是使用递归非常占用系统资源(只有进行没有出栈)，
所以使用递归需要谨慎.
'''