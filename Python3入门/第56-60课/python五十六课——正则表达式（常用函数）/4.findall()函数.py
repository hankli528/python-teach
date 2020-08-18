#！/usr/bin/env python
# Author:Hank
import re
'''
4).函数：findall(regex,string,[flags=0])：

参数：

和match、search一样理解

功能：

将所有匹配成功的子数据(子串)，以列表的形式返回；

如果一个都没有匹配成功，那么返回一个空列表
'''

'''
compile()配合search()使用：
'''
pat=re.compile(r'www')
matchobj=pat.search('www.sina.com!!www.baidu.com.com!!www')
# print(matchobj)


'''
函数：findall(regex,string,[flags=0]):
参数：
和match、search一样理解

功能：
将所有匹配成功的子数据(子串),以列表的形式返回;
如果一个都没有匹配成功，那么返回一个空列表
'''
# lt=re.findall(r'WWW','www.sina.com!!www.baidu.com!!www')
# lt=re.findall(r'WWW','www.sina.com!!www.baidu.com!!www',flags=re.I)
# print(lt,type(lt))

'''
compile()配合findall()使用：
'''
pat=re.compile(r'www',flags=re.I)
lt=pat.findall('www.sina.com!!www.baidu.com!!www')
print(lt)