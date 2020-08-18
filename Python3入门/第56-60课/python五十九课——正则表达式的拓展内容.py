#！/usr/bin/env python
# Author:Hank

import re
'''
演示正则表达式的拓展内容：
函数：
finditer(regex,string,[flags=0])：
参数：和match、search、findall一样理解
功能：
将所有匹配的数据封装为一个一个的match对象，
然后以iterator返回
'''

str1 = 'i love shanghai shanghai shanghai so much'
regex = 'shanghai'
it = re.finditer(regex,str1)
# print(it,type(it))

'''
iterator(迭代器对象)不能直接被len()所执行，否则报错：TypeError
但是我们可以将其先装换为容器对象(list、tuple...)可以被len()所执行了
'''
# print(len(it))
# print(len(list(it)))


'''
使用遍历的思想去访问iterator中的元素
'''
# for i in it:
    # print(i)
    # print(type(i))
    # print(i.group())

#迭代器对象中的内容只能被使用一次，不可逆；否则报错：StopIteration
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it)) #报错


'''
思考：可不可以使用while循环来实现遍历iterator对象的操作？
'''
while 1:
    try:
        matchobj=next(it)
        print(matchobj)
        print(matchobj.group())
    except:
        break