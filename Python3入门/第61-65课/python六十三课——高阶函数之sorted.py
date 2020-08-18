#！/usr/bin/env python
# Author:Hank

'''
演示sorted函数的使用，以及和sort的区别：
我们将sorted和sort进行一番比较：
相同点：
它们都是来实现排序的操作(功能层面)
不同点：
列表中的sort函数，它执行完毕后会直接影响原本这个list的内部结构(内部的数据发生改变了)；
而内置函数sorted函数，它执行完毕后不会影响原本容器中的内部结构，而会返回一个新的列表给程序；
回顾排序：
选择排序，冒泡排序它们的性能都很低下；
意味着开发不会用，但是面试喜欢面(一般开发不用的，面试都喜欢面)
'''
lt = [15,-13,0,-88,97,31,-5,27]
lt.sort()
# print(lt)

# lt1=sorted(lt,reverse=True)
# print(lt1,type(lt1))
# print(lt)

lt1=sorted(lt,key=abs,reverse=True)
# print(lt1)

lt2 = ['aaaaa','bb','ccccccc','ddddddddddd']
lt3=sorted(lt2,reverse=False,key=len)
# print(lt3)
# print(lt2)


#扩展
lt4 = [
 {'name':'大郎','age':40},
 {'name':'二郎','age':32},
 {'name':'金莲','age':23},
 {'name':'大官人','age':27},
 {'name':'王婆','age':60}
]

#年龄排序
lt5=sorted(lt4,reverse=False,key=lambda x:x['age'])
print(lt5)