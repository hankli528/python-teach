#！/usr/bin/env python
# Author:Hank

#演示list类型中常用的一些函数：

'''
1、append(obj)：将obj元素追加到列表的末尾
'''
lt=['路费','佐罗','山治','乔巴','乌索普','纳米桑']

#append():
lt.append('香克斯')
# print(lt,len(lt))

lt.append(['鸣人','佐助','樱','卡卡西'])
# print(lt,len(lt))




'''
2.extend(iterable)：将序列对象中的各个元素分别得到往列表的末尾追加
'''
lt.append(['鸣人','佐助','樱','卡卡西'])
# print(lt,len(lt))
lt.extend('大蛇丸')
# print(lt,len(lt))

'''
extend()函数参数只能接受iterable(可迭代对象),由于int不属于可迭代对象，
所以出错了,错误类型：TypeError
'''
# lt.extend(100)
# print(lt,len(lt))

'''
3、index(obj)：返回列表中obj元素首次出现的位置；如果obj不存在于列表中，报错
count(obj)：返回列表中obj元素一共出现了多少次；如果obj不存在于列表中，返回0
'''
lt=['路费','佐罗','山治','乔巴','乌索普','纳米桑','山治']
# print(lt.index('山治'))

'''
以下代码出错了：
原因：index()函数接受的时机参数如果不存在于列表中，只会报错：
'''
# print(lt.index('山治啊'))

# print(lt.count('山治'))

#对于count()函数而言，如果不匹配，不会报错，返回0
# print(lt.count('山治啊'))


'''
4、pop()：如果不传递参数，弹出列表最终的一个元素(返回值)；

如果传递参数，只能传递索引内容，将索引位置上的元素弹出

remove(obj)：删除列表中首次匹配成功的obj元素，没有返回值

clear()：清空列表
'''
lt2=['路费','佐罗','山治','乔巴','乌索普','纳米桑','山治']

# print(lt2.pop())
# print(lt2)

# lt2.pop(2)
# print(lt2)

'''
以下代码报错：
原因：pop()函数的参数只能接受索引值，不能接受实体内容
'''
# lt2.pop('乔巴')


# print(lt2.remove('乌索普')) #remove()函数执行完毕了，没有返回值
# print(lt2)
# print(lt2.remove('山治')) #remove()函数只能删除最先匹配成功的一个数据，不能删除多个
# print(lt2)

# lt2.clear()
# print(lt2)


'''
5、sort(reverse,key)：默认对于列表元素升序排列(reverse=False)，如果传入reverse=True就是降序排列了

reverse()：将列表中的元素进行反转
'''

lt3=[31,22,44,66,7,-11,24,5,-54,33]

# lt3.sort(reverse=True)
# print(lt3)

# lt3.reverse()
# print(lt3)


'''
6、copy()：拷贝列表内容，生成一个新的列表返回 -->浅拷贝

copy模块中有如下两个函数：

copy()：和list中的copy一样理解；--> 浅拷贝

deepcopy()：属于深拷贝
'''
import copy
'''
以下内容很重要，一定好好听...
谈论：浅拷贝和深拷贝
涉及的函数：
列表中的copy(),copy模块中的copy以及deepcopy()

浅拷贝：
        1).引用传递（地址传递） 代码：lt1=lt
        2).列表的copy()和copy模块中copy()也都是
        
深拷贝：
        copy模块中的deepcopy()
'''
lt4=[11,22,33,44,55,[1,2,3]]
lt5=lt4

lt6=lt4.copy()
lt7=copy.copy(lt4)
lt8=copy.deepcopy(lt4)

#lt4.append()
lt4[-1].append(4)
print(lt4,id(lt4)) #[11, 22, 33, 44, 55, [1, 2, 3, 4]] 15406704
print(lt5,id(lt5)) #[11, 22, 33, 44, 55, [1, 2, 3, 4]] 15406704
print(lt6,id(lt6)) #[11, 22, 33, 44, 55, [1, 2, 3, 4]] 15407464
print(lt7,id(lt7)) #[11, 22, 33, 44, 55, [1, 2, 3, 4]] 17373144
print(lt8,id(lt8)) #[11, 22, 33, 44, 55, [1, 2, 3]] 17428768

print(lt4)
print(lt5)
print(lt6)
print(lt7)
print(lt8)