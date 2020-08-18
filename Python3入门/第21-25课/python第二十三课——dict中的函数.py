#！/usr/bin/env python
# Author:Hank
'''
dic1 = {...}

dic2 = {...}

dic1.update(dic2)

1、update(dict)：dic1调用update传入dic2，如果dic2中的内容在dic1中不存在，那么直接加入新的价值对到dic1中；如果dic2中的键在dic1中已经出现了，那么就将dic2中键所对应的值去覆盖dic1中的键的值
'''
'''
演示dict类型中常用的一些函数：
'''
dic1={'name':'金毛狮王','age':45,'sex':'男','height':185.0}
dic2={'weight':100,'girlFriend':'灭绝师太','name':'青翼蝙王'}

#update()
# dic1.update(dic2)
# print(dic1)
# print(dic2)

'''
2、items()：返回一个dict_items类型的对象，对象中将键和值分别存入到元祖中，将元祖放入到items对象中

keys()：返回一个dict_keys类型的对象(简称键集)

values()：返回一个dict_values类型的对象(简称值集)
'''
its=dic1.items()
# print(its,type(its))

# for k in dic1:
#     print(k + '-->' + str(dic1.get(k)))
# print()

# for k,v in its:
#     print(k + '==>' +str(v))
# print()

k=dic1.keys()
# print(k,type(k))

# for k1 in k:
#     print(k1+'====='+str(dic1[k1]))
# print()


v=dic1.values()
# print(v,type(v))

# for v1 in v:
#     print(v1)

print('-'*50)



'''
3、pop(key)：传入key，返回value，弹出key-value对；如果key不存在，报错；

popitem()：将字典最后一个键值对弹出
'''
dic1={'name':'金毛狮王','age':45,'sex':'男','height':185.0}
# print(dic1.pop('name'))
# print(dic1)

'''
以下代码会报错：
对于dict的pop()函数必须传入存在的键，否则报错，错误类型为：KeyError
'''
# print(dic1.pop('name1'))

# print(dic1.popitem())
# print(dic1)

# dic2.clear()
# print(dic2)


#copy():
dic3=dic1.copy()
# print(dic1,id(dic1))
# print(dic3,id(dic3))