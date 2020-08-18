#！/usr/bin/env python
# Author:Hank
'''
1.生成器：

什么是生成器？

它内部封装了一套公式/算法，只有等到需要调用/执行数据时 --> next()函数执行

才会将公式计算得到数据结果，这就是生成器的原理(核心思想)；

【注意事项】：

1).生成器中是没有真实数据存在，所以我们是不能直接使用len()函数来尝试得到其长度

如果我们这么做了，会报错：StopIteration

2).生成器中关联的真实数据只能被使用一次，不可逆

格式：两种

执行返回一个generator类型对象

1).

(条件表达式 for 参数列表 in 容器对象)

2).

定义函数，在函数的内部需要使用yield关键字来记录返回的generator对象的数据公式，

【注意】函数此时如果有return，已经无视了/没有作用了，返回的一定是generator
'''

'''
演示生成器的定义和使用：
'''
#格式1：(条件表达式 for 参数列表 in 容器对象)
gen=(x for x in range(5))
# print(gen,type(gen))

#generator对象不能配合len()来获取其长度
# print(len(gen))

#使用next()函数来得到每一次genexpr中的内容
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


#generator对象中的数据内容只能被解析使用一次，不可逆；一旦调用多了，直接报错；
# StopIteration
# print(next(gen))

'''
以下是两种解析处理generator对象的方式：
方式一：使用next()函数调用，如果调多了，报错：StopIteration
方式二：使用循环处理，如果调多了，不会报错，什么都看不到-->这样的方式更加友好
'''
# print(next(gen))
# print(next(gen))
# for g in gen:
    # print('11111')
    # print(g)
    # print(next(g))
    # print('*'*50)

# for g in gen:
#     print(g)
# gen=(x for x in range(5))

'''
需求：思考如果对于gen对象中的真实数据我需要用到多次，那怎么办？
可以将generator对象gen转换为一个譬如list对象即可
'''
lt=list(gen)
# print(lt,type(lt))

# for i in lt:
#     print(i)
    # print('*'*50)

# i=0
# while i<len(lt):
#     print(lt[i])
#     i+=1


'''
格式2：
定义函数，在函数的内部需要使用yield关键字来记录返回的generator对象的数据公式，
【注意】函数此时如果有return,已经无视了/没有作用了，返回的一定是generator
'''
def func(n):
    lt=[]
    for i in range(1,n+1):
        if i%2==0:
            lt.append(i)
            yield i
    return lt

# f=func(10)
# print(f,type(f))

# print(len(f))

# print(next(f))

# for i in f:
#     print(i)

# print(list(f))

# print('*'*50)

# gen=(x for x in range(1,11) if x%2==0)
# for g in gen:
#     print(g)


#需求：实现全排列
str1='ABC'
str2='XYZ'
def func2(str1,str2):
    for s1 in str1:
        for s2 in str2:
            yield s1 + s2

# gen=func2(str1,str2)
# print(gen,type(gen))
#
# for g in gen:
#     print(gen)
#
# print('*'*50)

# gen=(x+y for x in str1 for y in str2)
# for g in gen:
#     print(g)


'''
比较：列表生成式和生成器？

对于生成器而言：

定义执行会得到一个generator对象，

此对象中没有真实数据(第一手没值)，它内部封装了一套公式/算法，

一旦需要使用数据了，就会计算公式，得到内容；

就因为这样的特点，所以我们得出结论：

1).生成器比较节省内存资源(好处)

2).在数据运算时比列表生成式效率要慢一点(弊端)

对于列表生成式而言：

定义执行会得到一个列表对象，

在定义执行完毕后，列表中已经确定了真实的数据(进内存了)

就因为这样的特点，所以我们得出结论：

1).列表生成式比较占用内存资源(弊端)

2).在数据运算时比生成器效率要快一点(好处)
'''