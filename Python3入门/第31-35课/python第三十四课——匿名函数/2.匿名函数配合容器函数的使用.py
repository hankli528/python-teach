#！/usr/bin/env python
# Author:Hank

'''
匿名函数配合容器函数的使用(了解)
'''

#1.匿名函数配合列表对象使用
lt=[lambda x:x**2,lambda x:x**3,lambda x:x**4]

for i in lt:
    print(i(2))

print(lt[2](3))

print('*'*50)


#2.匿名函数配合字典对象使用
key='B'

dic1={
    'A':lambda :2*2,
    'B':lambda :3*3,
    'C':lambda :4*4
}
print(dic1[key]())

dic2=[
    {'name':'张学友','age':56,'height':172.0},
    {'name':'刘德华','age':51,'height':176.0},
    {'name':'郭富城','age':55,'height':169.0},
    {'name':'黎明','age':53,'height':180.0},
]

#需求：按照人物的身高降序排序到列表中的数据
dic2.sort(key=lambda x:x['height'])
print(dic2)