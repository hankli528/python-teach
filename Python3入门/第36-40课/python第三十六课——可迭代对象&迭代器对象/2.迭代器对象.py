#！/usr/bin/env python
# Author:Hank

'''
满足前提：

1).必须是一个可迭代对象

2).可以被next()所作用的

举例：

generator...

高效的检测一个对象是否是迭代器对象

需要使用collections模块中的Iterator类配合isinstance()内置函数来判断

步骤如下：

第一步：导入collections模块

第二步：collections.Iterator(类型)配合isinstance()函数来判断，代码如下：

isinstance(obj,collections.Iterator)

如果返回值为True，那么它就是一个迭代器对象

如果返回值为False，那么它就不是一个迭代器对象

将可迭代对象转换为迭代器对象

内置函数：iter()

【注意】此函数必须只能调用可迭代对象，否则报错
'''
import collections
'''
演示是否是迭代器对象
'''
str1 = 'abcd'
lt = [1,2,3,4]
tp = (11,22,33)
s = {100,200,300,400}
dic1 = {'AA':'aa','BB':'bb'}
r = range(10)
gen = (x for x in range(5))
# print(isinstance(str1,collections.Iterator))
# print(isinstance(lt,collections.Iterator))
# print(isinstance(tp,collections.Iterator))
# print(isinstance(s,collections.Iterator))
# print(isinstance(dic1,collections.Iterator))
# print(isinstance(r,collections.Iterator))
# print(isinstance(gen,collections.Iterator))

'''
以下代码报错了:只有Iteratot对象才能被next()函数所调用
'''
# print(next(lt))


'''
将可迭代对象转换为迭代器对象
内置函数：iter()
【注意】此函数必须只能调用可迭代对象，否则报错
'''
gen1=iter(lt)
print(gen1,type(gen1))

gen2=iter(tp)
print(gen2)

print(next(gen1))
print(next(gen2))

'''
以下代码有问题：
因为100是int类型数据，它并不是一个Iterable(可迭代对象),
所以不能被iter()转换成为Iterator(迭代器对象)
'''
# gen3=iter(100)
# print(gen3,type(gen3))