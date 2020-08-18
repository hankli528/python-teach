#！/usr/bin/env python
# Author:Hank
'''
1.random()：返回一个[0,1)的随机浮点数(双精度浮点数)

2.uniform(a,b): 返回[a,b]之间的一个随机浮点数(双精度浮点数)

【注意】a和b接受的数据大小随意 例如：3.random.uniform(10,20) random.uniform(20,10)

4.randrange(start,end,step):返回[start,end)之间的一个随机整数

5.randint(a,b)：返回[a,b]之间的一个随机整数

6.choice(seq)：传递的是一个序列对象，返回seq中的一个随机元素

7.sample(seq,number)：从seq中随机取出number个元素，以列表的形式返回

8.shuffle(lt)：将lt(列表对象)中的元素打乱
'''

import random

#random():
# print(random.random())
# print(round(random.random(),3))

#uniform():
# print(random.uniform(10,20))
# print(random.uniform(20,10))
# print(random.uniform(30,30))

#randrange(start,end,step):
# print(random.randrange(0,10,2))

#choice(seq):
# print(random.choice([1,2,3,4,5]))

#sample(seq,number):
# print(random.sample('我是一个程序员',3))

#randint(a,b):
# print(random.randint(1,3))

#shuffle(lt):
lt=['a','b','c','d','e','f']
# lt=tuple(lt)
random.shuffle(lt) #类似洗牌
print(lt)