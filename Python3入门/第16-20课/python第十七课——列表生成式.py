#！/usr/bin/env python
# Author:Hank
'''
1.列表生成式：

什么是列表生成式？

它就是一串表达式，专门用于生成列表对象，当中包含一系列的业务逻辑；

结构：简介、优雅、阅读性好；比传统获取列表对象来的更加的方便；

它是语法糖的一种；

什么是语法糖？

我们在实际开发中，碰到比较复杂的业务逻辑，

可能导致代码的书写量就上去，语法糖的出现就是在不破坏复杂业务逻辑的同时，

使用更加简便、少的代码量来完成一样的需求，

从而解放程序员，让你享受编码的快感...

格式：

[expr for ver1,[ver2] in 序列对象(str、range、list、tuple、set、dict...) if ...]
'''

'''
演示列表生成式的使用以及好处:
'''
#需求1：生成1~10的列表

#方式一：不使用列表生成式的方式
# print(list(range(1,11)))

#方式二：使用列表生成式的方式
# print([x for x in range(1,11)])


#需求2：生成1+1,2+2,3+3,...,10+10的一个列表
#方式一：不使用列表生成式的方式
lt1=[]
for i in range(1,11):
    lt1.append(i**2)
# print(lt1)

#方式二：使用列表生成式的方式
# print([x**2 for x in range(1,11)])


#需求3：生成1+1,2+2,3+3,...,10+10中只保留偶数的乘积值到列表中
#方式一：不使用列表生成式的方式
lt2=[]
# for i in range(1,11):
#     if i%2==0:
#         lt2.append(i**2)
# print(lt2)

for i in range(1,11):
    if i%2!=0:
        lt2.append(i**2)
# print(lt2)

#方式二：使用列表生成式的方式
# print([x ** 2 for x in range(1,11) if x%2==0])


#需求4：实现全接列
'''
a='ABC'
b='XYZ'

效果如下：
['AX','AY','AZ','BX',...,'CZ']
'''
a='ABC'
b='XYZ'
#方式一：不使用列表生成式的方式
lt3=[]
for i in a:
    for j in b:
        lt3.append(i+j)
# print(lt3)

#方式二：使用列表生成式的方式
# print([x+y for x in a for y in b])


#需求5：将字典对象中的键和值得到作为一个元素，存入到列表对象中
'''
dic={'AA':'aa','BB':'bb','CC':'cc',}

效果如下：
['AA=aa','BB=bb','CC=cc']
'''
dic={'AA':'aa','BB':'bb','CC':'cc'}
#方式一：不使用列表生成式的方式
lt4=[]
for k,v in dic.items():
    lt4.append(k +'='+v)
# print(lt4)

#方式二：使用列表生成式的方式
# print([k + '=' + v for k,v in dic.items()])


#需求6：将lt=['PYTHON','Java','PHP','UI']中的元素内容都转换小写，然后保存到一个列表中返回
lt=['PYTHON','Java','PHP','UI']
#方式一：不使用列表生成式的方式
lt5=[]
for i in lt:
    lt5.append(i.lower())
# print(lt5)

#方式二：使用列表生成式的方式
# print([x.lower() for x in lt])


#需求7：将lt=['PYTHON','Java','PHP','UI',100]中的元素内容都转换小写，然后保存到一个列表中返回
lt=['PYTHON','Java','PHP','UI',100]

'''
以下代码会出错：
因为lt列表对象中不仅只有str类型的数据，还有int类型的数据。
而lower()函数是属于str中独有的函数，其他类型不会调用；
异常类型：AttributeError

解决方式如下:
我们可以先使用内置函数isinstance(obj,type),如果返回True,表示类型匹配：
反之，不匹配，返回False
'''

# print([x.lower() for x in lt])
print([x.lower() for x in lt if isinstance(x,str)])