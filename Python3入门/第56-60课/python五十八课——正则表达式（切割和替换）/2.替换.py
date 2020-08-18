#！/usr/bin/env python
# Author:Hank

'''
替换：
sub(regex,repl,string,count,[flags=0])：
 替换数据，返回字符串(已经被替换完成后的内容)
subn(regex,repl,string,count,[flags=0])：
 替换数据，返回元祖对象，此元祖有两个元素
 第一个元素记录了替换以后的字符串内容，
 第二个元素记录了被替换的次数(count的值)
参数：
regex：正则规则(字符串)
repl：需要被替换成的内容(new)
string：需要被替换的内容(原串)
count：需要被替换的个数，默认全部替换
'''
import re

str1='i love shenzhen shenzhen shenzhen so much'
regex=r'(shenzhen)'

str2=re.sub(regex,'shanghai',str1)
# print(str2,type(str2))

obj=re.subn(regex,'shanghai',str1,2)
# print(obj,type(obj))



'''
需求：
实现让游戏世界变得和谐（正则表达式）
'''
regex=r'WQNMLGB|CNM|MB|SB|NC|TMD|NND'
game='WQNMLGB!!连装备都不会出...小学生!!SB'
s=re.sub(regex,'***',game)
print(s)