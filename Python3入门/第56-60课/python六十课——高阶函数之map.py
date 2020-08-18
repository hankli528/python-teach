#！/usr/bin/env python
# Author:Hank

'''
1.高阶函数：

特点：函数的形参位置必须接受一个函数对象

分类学习：

1).map(fn,lsd1,[lsd2...])：

参数一：fn --> 函数对象

参数二：lsd1 --> 序列对象(字符串、列表、range...)

功能：

将fn函数作用于lsd1中的每一个元素上,

将每次执行的结果存入到一个map对象中返回；

【注意】得到的这个map对象是一个迭代器对象

需求：lt = ['1','2','3','4','5'] --> [1,2,3,4,5]

map(int,lt)：执行过程如下：

1).lt --> 取出第一个元素：'1'当做实际参数传递给int函数的形参位置 --> int('1')

将转换以后的结果：1保留到map对象的第一个元素位置

2).lt --> 取出第二个元素：'2'当做实际参数传递给int函数的形参位置 --> int('2')

将转换以后的结果：2保留到map对象的第二个元素位置

以此类推...

直到map函数执行完了，整个map对象才真正成型了...
'''
import collections
'''
高阶函数之：
map(fn,lsd1,[lsd2,...])
参数一：fn --> 函数对象
参数二：lsd1 --> 序列对象(字符串、列表、range...)
功能：
将fn函数作用于lsd1中的每一个元素上,
将每次执行的结果存入到一个map对象中返回；
【注意】得到的这个map对象是一个迭代器对象
'''
#需求：lt = ['1','2','3','4','5'] --> [1,2,3,4,5]
lt = ['1','2','3','4','5']

#代码实现一：使用老技术来实现
lt1 = []
for i in lt:
    num=int(i)
    lt1.append(num)
#由于列表对象是非惰性序列，可以直接打印看到内容
# print(lt1)

#代码实现二：使用新技术解决
#步骤一：定义一个函数功能：将str数据-->int数据
def chr2Int(chr):
    # return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[chr]
    return int(chr)

mo=map(chr2Int,lt)

'''
map类型的对象在打印过程中不能直接看到其中的元素值，
所以map对象是一个惰性序列对象
'''
# print(mo,type(mo))
# print(isinstance(mo,collections.Iterator))

# print(next(mo))
# print(next(mo))

'''
将map对象(惰性的)转换为list对象(非惰性的)
'''
# print(list(mo))

#代码实现三：终极版(一步到位)
# print(list(map(chr2Int,lt)))
# print(list(map(int,lt)))

'''
代码：
map(int,lt)：执行过程如下：
1).lt --> 取出第一个元素：'1'当做实际参数传递给int函数的形参位置 --> int('1')
 将转换以后的结果：1保留到map对象的第一个元素位置
2).lt --> 取出第二个元素：'2'当做实际参数传递给int函数的形参位置 --> int('2')
 将转换以后的结果：2保留到map对象的第二个元素位置 
以此类推...
直到map函数执行完了，整个map对象才真正成型了... 
'''

#需求1：lt = [1,2,3,4,5] --> 效果：['1','2','3','4','5']
#需求2：lt = [1,2,3,4,5] --> 效果：[1,4,9,16,25]
lt=[1,2,3,4,5]
#自定义函数：将int-->str
def int2Str(i):
    return str(i)
# print(list(map(int2Str,lt)))
# print(list(map(str,lt)))
# print(list(map(lambda x:str(x),lt)))

#自定义函数：实现开方操作
def kaifang(num):
    return num**2
# print(list(map(kaifang,lt)))
# print(list(map(lambda x:x**2,lt)))