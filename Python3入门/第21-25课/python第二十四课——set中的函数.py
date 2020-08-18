#！/usr/bin/env python
# Author:Hank

#集合中常用的一些函数：

'''
1、add(obj)：追加一个obj元素到集合中

pop()：从集合中随机弹出一个元素

remove(obj)：删除集合中和obj匹配的元素

clear()：清空集合
'''
s1={10,100,3.14,'abcd'}
# s1.add('haha')
# print(s1.pop())
# s1.remove('abcd')
# s1.clear()

'''
以下代码有问题：
set中的pop只能是空的函数，不能传递内容和索引，一传就错...错误类型：TypeError
'''
# print(s1.pop(10))


'''
2、以下函数使用s1调用，传入s2

issuperset()：判断s1是否是s2的父集；返回布尔值

issubset()：判断s1是否是s2的子集；返回布尔值

isdisjoint()：判断s1和s2是否有交集，如果有，返回False；反之，返回True
'''
s2={1000,'abcde'}
# print(s1.issuperset(s2))
# print(s1.issubset(s2))
# print(s1.isdisjoint(s2))