#！/usr/bin/env python
# Author:Hank
'''
自定义函数实现swapcase的效果
'''

str1='abcdEFG123##abCD'
str2='1234567'
str3='abcd'
def my_swapcase(s):
    s1=""
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            s1 += chr(ord(i) + 32)
        elif ord(i) >= 97 and ord(i) <= 122:
            s1 += chr(ord(i) - 32)
        else:
            s1 += 1
    return s1

#调用自定义函数
a=my_swapcase(str3)
print(a)