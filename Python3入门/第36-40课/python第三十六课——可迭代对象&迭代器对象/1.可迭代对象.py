#！/usr/bin/env python
# Author:Hank

'''
1.可迭代对象：

满足前提：

只要能被循环操作的对象，就可以可迭代对象

举例：

str、list、tuple、set、dict、range、generator...

高效的检测一个对象是否是可迭代对象

需要使用collections模块中的Iterable类配合isinstance()内置函数来判断

步骤如下：

第一步：导入collections模块

第二步：collections.Iterable(类型)配合isinstance()函数来判断，代码如下：

isinstance(obj,collections.Iterable)

如果返回值为True，那么它就是一个可迭代对象

如果返回值为False，那么它就不是一个可迭代对象
'''
import collections
'''
演示判断是否是可迭代对象
'''
str1 = 'abcd'
lt = [1,2,3,4]
tp = (11,22,33)
s = {100,200,300,400}
dic1 = {'AA':'aa','BB':'bb'}
r = range(10)
gen = (x for x in range(5))
print(isinstance(str1,collections.Iterable))
print(isinstance(lt,collections.Iterable))
print(isinstance(tp,collections.Iterable))
print(isinstance(s,collections.Iterable))
print(isinstance(dic1,collections.Iterable))
print(isinstance(r,collections.Iterable))
print(isinstance(gen,collections.Iterable))