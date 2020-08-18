#！/usr/bin/env python
# Author:Hank
'''
2.ascii码

美国设计出来的一张编码表，将涉及的字符都编号了，底层仍然还是进行二进制的运算；

记住：3个范围段

1).'0' --> 码值：48

2).'A' --> 码值：65

3).'a' --> 码值：97

内置函数：

1).ord(str)：将str转换为码值(整数类型)

2).chr(num)：将码值num转换为字符
'''

'''
演示：ord()和chr()内置函数的作用：
'''
num=48
c=chr(num)
print(c,type(c))
print(ord(c),type(ord(c)))

'''
案例：从键盘读入内容，如果是小写字母输出大写，如果是大写输出小写
'''
content=input('请输入英文字符：')
if ord(content) >= 65 and ord(content) <= 90:
    print(content+'的小写字符为：%s' %(chr(ord(content) + 32)))
else:
    print(content+'的大写字符为：%s' %(chr(ord(content) - 32)))
