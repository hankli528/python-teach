#！/usr/bin/env python
# Author:Hank
'''
函数：search(regex,string,[flags=0])：
参数：
和match一样理解
功能：
从头开始匹配字符串中的数据，如果头不匹配继续往后尝试匹配，
直到有第一个匹配成功的子数据，立即返回一个match对象；此时就算后面还有匹配的子数据，直接无视...
当然匹配不成功，返回None值
【注意】：
由于search调用完毕之后返回的仍然是一个match对象，所以还是可以调用5个常用的函数
'''
import re

# print(re.match(r'www','hahawww.baidu.com!!www.qfedu.comhehe'))
# print(re.search(r'www','hahawww.baidu.com!!www.qfedu.comhehe'))
# print(re.search(r'www','hahawww.baidu.com!!www.qfedu.comhehe').group())

# print(re.search(r'www','hahahwww.baidu.com!!www.qfedu.comhehe').start())
# print(re.search(r'www','hahahwww.baidu.com!!www.qfedu.comhehe').end())

# print(re.search(r'www','hahahwww.baidu.com!!www.qfedu.comhehe').span())
# print(re.search(r'www','hahahwww.baidu.com!!www.qfedu.comhehe').groups())

# print(re.search(r'Www','hahahwww.baidu.com!!Www.qfedu.comhehe'))
# print(re.search(r'Www','hahahwww.baidu.com!!Www.qfedu.comhehe',flags=re.I))


