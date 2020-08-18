#！/usr/bin/env python
# Author:Hank

'''
验证邮箱：
参考：heixuanfeng_lg@163.com
满足的条件如下：
1).@符号前面的内容可以包含数字、英文和_数据，其长度控制在[6,18]位
2).@符号后面的内容可以包含数字和英文，其长度控制在[2,8]位
3).点(.)不能拥有元字符的含义
4).点(.)后面的内容只能包含com|cn
'''
import re

regex = r'w{6,18}@[0-9a-zA-Z]{2,8}.(com|cn)'
pat=re.compile(regex)
str1='heixuanfeng_lg@163.cn'
# print(pat.match(str1))


'''
验证手机号：
需求：
1.长度必须是11位
2.必须都是数字字符
3.第一位1开头，第二位：345789
'''
phone='13995995995'
regex = 'A1[345789]d{9}Z'
# print(re.match(regex,phone))

