#！/usr/bin/env python
# Author:Hank

'''
演示正则中的替换和切割操作：
在这之前我们先学习一个分组的概念：
'''
'''
分组：
在正则中定义(...)就可以进行分组，理解为得到了一个子组
好处：
1).如果正则中的逻辑比较复杂，使用分组就可以优化代码的阅读性(更有层级感)
2).一旦进行了分组，在正则表达式的后半部分内容中很有可能需要引用子组中的内容；
 一旦引用了组，那么这两部分的内容(值)就可以保持一致了
'''
import re
phone='62589999'
regex=r'd{4}(d)r{3}' #r'...()...()...()..'
# print(re.match(regex,phone))
# print(re.match(regex,phone).groups())
# print(re.match(regex,phone).group())
# print(re.match(regex,phone).group(0))
# print(re.match(regex,phone).group(1))

'''
以下代码有问题：
出现了下标越界的异常：IndexError
原因为正则中只有1个子组，没有index=2这一说，所以报错了...
'''
# print(re.match(regex,phone).group(2))

phone = '021-52184329'
regex = r'(?P<one>d{3})(?P<two>-)(?P<three>d{8})'
mathobj=re.search(regex,phone)

# print(mathobj.groups())
# print(mathobj.group())
# print(mathobj.group(0))
# print(mathobj.group('one'))
