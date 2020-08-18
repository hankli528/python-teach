#！/usr/bin/env python
# Author:Hank
from functools import reduce
'''
总结：高阶函数以及匿名函数之间的配合使用
'''
#模块一：lambda和filter的结合使用
#lt = [1,2,3,4,5,6,7,8,9] --> [3,6,9]]
# lt = [1,2,3,4,5,6,7,8,9]
# print(list(filter(lambda x:x%3==0,lt)))


#模块二：lambda和map的结合使用
#容器/序列对象：range对象
mo=map(lambda x:x**2,range(5))
# print(list(mo))

#模块三：
'''
在模块二的基础上扩展功能:range(10)
过滤以后保留的数据范围为：(5,50)之间
'''
mo=map(lambda x:x**2,range(10))
fo=filter(lambda x:x>5 and x<50,mo)
# print(list(fo))


#模块四：lambda和reduce配合使用
lt=[1,2,3,4,5]
my_sum=reduce(lambda x,y:x+y,lt)
print(my_sum)
