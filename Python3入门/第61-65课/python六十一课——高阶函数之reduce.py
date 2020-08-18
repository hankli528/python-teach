#！/usr/bin/env python
# Author:Hank
'''
2).reduce(fn,lsd)：

参数一：fn --> 函数对象

参数二：lsd --> 序列对象

功能：

先将lsd中的第一和第二个元素去除传入到fn中参与运算，

运算后得到结果，再和第三个元素传入到fn中参与运算，

以此类推...

【注意】：

reduce函数属于functools模块中的函数，所以需要显示的先导入functools模块再使用

from functools import reduce
'''

from functools import reduce
# lt=[1,2,3,4]
'''
lt = [1,2,3,4]
自定义封装函数 --> add 作用：对列表中的元素求和 def add(x,y)
使用reduce函数执行效果如下：
第一次：add(1,2)
第二次：add(add(1,2),3)
第三次：add(add(add(1,2),3),4)
'''
#需求：计算列表中元素的和值
lt=[1,2,3,4]
#代码实现一：；递归解决求和的问题（简单递归）
# def mySum(num):
#     if num==1:
#         return 1
#     return num+mySum(num-1)
# print(mySum(4))

#代码实现二：新技术(reduce)
def add(x,y):
    return x+y
res=reduce(add,lt)
# print(res,type(res))
# print(reduce(lambda x,y:x+y,lt))
# print(sum(lt))

#需求：lt=[1,2,3,4]得到其中元素的乘积
# print(reduce(lambda x,y:x*y,lt))


'''
需求：
从键盘读入一个整数字符串，例如：'12345'
需要将其转换为12345，注意：不能直接使用int()来实现
思路：使用map和reduce配合来实现
步骤一：'12345' --> 拆分为散装数据：1 2 3 4 5 可以用map来实现
步骤二：将map对象中的数据1 2 3 4 5组合成为 --> 12345 可以用reduce来实现
'''
str1='12345'
def chr2Int(str):
    return int(str)

def func(x,y):
    return x*10+y
mo=map(chr2Int,str1)
num=reduce(func,mo)
print(num,type(num))

#终极版
print(reduce(lambda x,y:x*10 + y,map(int,str1)))