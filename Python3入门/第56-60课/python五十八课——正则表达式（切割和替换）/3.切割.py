#！/usr/bin/env python
# Author:Hank

'''
切割：
split(regex,string)：返回一个列表对象
'''
import re

# str1='i love shenzhen so much'
# regex=r' +?'
# lt=re.split(regex,str1)
# print(lt)

# str2='dsafsa2341241dfakdsf34242dsafasfd______3214123fdsafas2131dsafas'
# regex=r'd+'
# lt=re.split(regex,str2)
# print(lt)

'''
补充案例：和替换有关
需求：将如下字符串中的#替换为-
思考：
    1).一个#替换成一个-
    2).一堆#替换成一个-
'''

str3='dasf######dsaf2341dsaf13#####$%^&*___####fdasjkf2341as'
regex=r'#'
s=re.sub(regex,'-',str3)
# print(s)

regex=r'#+'
s=re.sub(regex,'-',str3)
# print(s)

