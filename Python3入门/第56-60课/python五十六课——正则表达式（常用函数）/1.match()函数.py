#！/usr/bin/env python
# Author:Hank
import re
'''
演示re模块中最常用的4个函数：
'''
'''
函数：match(regex,string,[flags=0])
参数：
regex：就是正则表达式(定义了一套验证规则)
string：需要被验证的字符串数据
flags：模式/标志位，默认情况下(不定义) --> 不开启任何的模式
功能：
从头开始尝试匹配字符串数据(注意：如果开头就不匹配直接返回None值)，
如果匹配成功，那么就会返回一个match对象；
如果匹配不成功，那么就会返回None值
flags的取值：
re.I：忽然大小写
match对象有5个常用的函数：
group()：返回匹配成功的数据(原串中的某子串数据)
start()：返回匹配成功的数据的起始索引
end()：返回匹配成功的数据的结束索引
span()：返回一个元祖对象，有两个元素组成；
 第一个元素记录了匹配成功的起始索引
 第二个元素记录了匹配成功的结束索引
groups()：返回所有子组的信息，以元祖的形式返回；如果没有分组，返回空元祖对象
【注意事项】：
 1).正则表达式返回的索引值需要满足含头不含尾的特点
 2).正则表达式验证的数据内容严格区分大小写
 3).我们之后在定义正则规则的时候，在引号前面+一个r，无脑操作...
'''

matchobj=re.match(r'www','www.baidu.com')
# print(matchobj,type(matchobj))

# print(re.match(r'www','www.sina.com'))
# print(re.match(r'www','www.sina.com').group())
# print(re.match(r'www','www.sina.com').start())
# print(re.match(r'www','www.sina.com').end())
# print(re.match(r'www','www.sina.com').span())
# print(re.match(r'www','www.sina.com').groups())
# print(re.match(r'WWW','www.sina.com'))
# print(re.match(r'WWW','www.sina.com',flags=re.I))

'''
使用第二种方式实现正则对数据的验证：
compile(regex,[flags=0]):返回一个Pattern对象(认为：它内部已经封装了一套regex和flags)
可以再通过Pattern对象继续调用match函数（此时只需要传递一个参数：string即可）
注意：
以上函数中涉及的参数：regex、flags、string和re.match中的参数一样理解
'''
pat=re.compile(r'www',flags=re.I)
# print(pat,type(pat))
# print(pat.match('wWw.baidu.com'))


