#！/usr/bin/env python
# Author:Hank

import re

'''
1.分析以下需求，并用代码实现：
 (1)定义一个存放手机号码的数字字符串列表["16210626656","18601066888","13912387666","13156166693","15115888028"]
 (2)利用正则表达式过滤出符合条件的手机号码，
 规则：第1位是1，第二位可以是数字358其中之一，后面6位任意数字，最后3位为任意相同的数字。
'''
phone_list=["16210626656","18601066888","13912387666","13156166693","15115888028"]
regex=r'^1[358]d{6}(d)r{2}$'

#定义lt来存储满足的手机号数据
lt=[]

#循环遍历phone_list列表对象
for phone in phone_list:
    if re.match(regex,phone):
        lt.append(phone)

#代码执行到此处了，说明lt中已经记录了满足的所有手机号信息
print(lt)
print([x for x in phone_list if re.match(regex,x)])