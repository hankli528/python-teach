#！/usr/bin/env python
# Author:Hank
'''
定义两个变量，交换它们的值(面试题)
使用第三方变量来实现
'''
a=10
b=20

print('交换前：a=%d, b=%d' %(a,b))

a,b=b,a
print('交换后：a=%d, b=%d' %(a,b))