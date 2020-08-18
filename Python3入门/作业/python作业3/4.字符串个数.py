#！/usr/bin/env python
# Author:Hank
'''
从键盘输入字符串，得到大写英文字符、小写英文字符、数字字符和其它字符的个数
'''

dx=0
xx=0
sx=0
qx=0

str1=input('请输入字符串：')

for s in str1:
    if ord(s) >= 65 and ord(s) <= 90:
        dx += 1
    elif ord(s) >= 97 and ord(s) <= 122:
        xx += 1
    elif ord(s) >= 48 and ord(s) <= 57:
        sx += 1
    else:
        qx += 1

print('大写字母有%d个' %dx)
print('小写字母有%d个' %xx)
print('数字字符有%d个' %sx)
print('其他字符有%d个' %qx)