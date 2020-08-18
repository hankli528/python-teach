#！/usr/bin/env python
# Author:Hank

'''
演示匹配多个字符：
以下x、y、n都是变量名：
分类：
1).模糊匹配：

x?：表示0个或者1个 取值范围：[0,1]
x+：表示1个或者多个 取值范围：[1,无穷大)
x*：表示0个或者多个 取值范围：[0,无穷大)
【注意】
以上三种符号(?、+、*)都满足贪婪匹配的特点，
意味着在匹配的前提下，尽可能多的返回数据
思考：如果取消贪婪行为？ --> 达到的效果就是在匹配的前提下，尽可能少的返回数据
代码体现：在正则的最后显示的定义一个?即可
2).精确匹配：
n{x}：n匹配x次
n{x,}：n最少有x次，最多无穷大 范围：[x,无穷大)
n{x,y}：n最少有x次，最多有y次 范围：[x,y]
'''
import re

print('--------------------------------演示匹配多个字符---------------------------------')

str1='bbbbbbbbbbbcccbbbb'
print(re.search(r'b?',str1).group())
# print(re.search(r'b??',str1).group())
# print(re.search(r'b+',str1).group())
# print(re.search(r'b+?',str1).group())
# print(re.findall(r'b?',str1))
# print(re.findall(r'b?',str1))
# print(re.findall(r'b+',str1))
# print(re.findall(r'b+?',str1))
# print(re.findall(r'b*',str1))
# print(re.findall(r'b*?',str1))

#需求：尝试匹配内容：hank ... man
# str1='hank is a good man hank is a nice man hank is a cool man'
# regex=r'hank.*man'
# regex=r'hank.*?man'
# lt=re.findall(regex,str1)
# print(lt)
# print(re.search(regex,str1).group())
# print('实现精准匹配...')

str1='aaaabbbaaaaaaaaaaaa'
# print(re.findall(r'a{3}',str1))
# print(re.findall(r'a{3,}',str1))
# print(re.findall(r'a{3,}?',str1))
# print(re.findall(r'a{6,8}',str1))
# print(re.findall(r'a{6,8}?',str1))