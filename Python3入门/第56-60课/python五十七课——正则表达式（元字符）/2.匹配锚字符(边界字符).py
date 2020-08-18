#！/usr/bin/env python
# Author:Hank
import re
'''
演示匹配锚字符(边界字符)
^：从字符串头部开始匹配，在开启多行模式下(re.M)，可以尝试匹配每一行的头部数据
$：从字符串尾部开始匹配，在开启多行模式下(re.M)，可以尝试匹配每一行的尾部数据
A：从字符串头部开始匹配，在开启多行模式下(re.M)，没有多行的概念，还是匹配第一行的头
Z：从字符串尾部开始匹配，在开启多行模式下(re.M)，没有多行的概念，还是匹配最后一行的尾
：匹配边界(左、右)，如果满足返回对象(match、list)
B：先舍弃边界数据，然后一定是从左侧开始匹配...
'''
print('---------------------------------演示匹配锚字符(边界字符)-----------------------------------')

# print(re.search(r'^www','hahawww.baidu.comhehe'))
# print(re.search(r'^haha','hahawww.baidu.comhehe'))
# print(re.search(r'hehe$','hahawww.baidu.comhehe'))
# print(re.search(r'com$','hahawww.baidu.comhehe'))
# print('-'*50)
#
# print(re.search(r'Awww','hahawww.baidu.comhehe'))
# print(re.search(r'Ahaha','hahawww.baidu.comhehe'))
# print(re.search(r'heheZ','hahawww.baidu.comhehe'))
# print(re.search(r'comZ','hahawww.baidu.comhehe'))


print('验证匹配字符串首位字符的区别：')
str1='''
hank is a cool man
hank is a nice man
hank is a prefect man
'''

# print(re.findall(r'hank',str1,flags=re.M))
# print(re.findall(r'leo',str1,flags=re.M))
# print(re.findall(r'man$',str1,flags=re.M))
# print(re.findall(r'manZ',str1,flags=re.M))
# print('*'*60)
# print(re.search(r'ne','never'))
# print(re.search(r'ne?','never'))
# print(re.search(r'er?','never'))

print(re.search(r'erB','never'))
print(re.search(r'erB','nerver'))
print(re.search(r'erB','ernerver'))
print(re.search(r'Ber','ernerver'))

