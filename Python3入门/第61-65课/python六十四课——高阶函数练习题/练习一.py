#！/usr/bin/env python
# Author:Hank

from functools import reduce
'''
1.lt = ['sdfasdfa', 'ewqrewrewqr', 'dsafa12312fdsafd', 'safsadf']
 --> 得到长度列表
2.tp = ('TOM', 'Lilei', 'JAck'， ‘HanmeiMeI’)
 --> 得到列表(所有元素的首字母大写)
3.
lt1 = [1,2,3,4]
lt2 = [5,6,7,8]
计算得到：lt1[0]lt2[0] + lt1[1]lt2[1] + ...
 15 + 26 +
最终得到累加以后的值
'''
lt = ['sdfasdfa', 'ewqrewrewqr', 'dsafa12312fdsafd', 'safsadf']
# print(list(map(len,lt)))

tp = ('TOM', 'Lilei', 'JAck','HanmeiMeI')

#自定义函数：
def func(name):
    return name.capitalize()

# print(list(map(func,tp)))
# print(list(map(lambda x:x.capitalize(),tp)))
# print(list(map(str.capitalize,tp)))

lt1=[1,2,3,4,5]
lt2=[5,6,7,8]

#使用map的思想得到组合数据对象(map类型)，对象中的元素内容为：15 26 37 48
lt1_map=map(lambda x:x*10,lt1) #map中的内容为：10,20,30,40
ret_map=map(lambda x,y:x+y,lt1_map,lt2) #map中的内容为：15,26,37,48
# print(list(ret_map))


#使用reduce的思想将map对象中的数据进行累加
num=reduce(lambda x,y: x + y,ret_map)
print('和值为： %s' %num)
