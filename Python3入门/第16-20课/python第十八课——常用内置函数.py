#！/usr/bin/env python
# Author:Hank

#常用内置函数：


#round():
# print(round(3.14),round(3.99))
# print(round(3145.926,-2),round(413.575,2))

# abs():
# print(abs(-2),abs(-1),abs(0),abs(1),abs(2))

#max()、min()、sum()
# print(max([1,2,3,4,5]))
# print(min([1,2,3,4,5]))
# print(sum([1,2,3,4,5]))

#以下比较的是字符串中每个字符的ascii值得大小
# print(min('abcdefghijkl12345678'))
# print(min(('a','0','A')))

'''
以下比较的是集合中键的大小，但是代码过于扯淡，开发不会用
'''
# print(min({'a':'haha','A':'haha','0':'heihei'}))
# print(min(1,2,3,4,5))
# print(min(range(3,10)))
# print(min('a','b','c'))

'''
对于min()、max()而言，参数既可以接受容器对象，也能接受多个单值数据
（需要保证数据类型统一）
'''
# print(min(1,2,3,4,5,'a'))


# print(sum([1,2,3,4,5]))
# print(sum([11,22,33,44,55]))

# print(sum(range(1,6)))


#3.bin()、oct()、hex()、power()、divmod()
# print(bin(100),type(bin(100)))
# print(oct(100))
# print(hex(100))
#
# print(pow(3,3))
# print(divmod(10,3))
#
