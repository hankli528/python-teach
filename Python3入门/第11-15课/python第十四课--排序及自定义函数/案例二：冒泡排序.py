#！/usr/bin/env python
# Author:Hank

#案例二：冒泡排序
lt1=[45,12,56,-32,-3,44,75,-22,100]
# print('排序前：'+str(lt1))

'''
自定义函数：实现冒泡排序（升序）
原则：
1).有没有形参？
有，接受一个列表对象

2).有没有返回值？
没有，排完就排完
'''
# def bubbleSort(lt):
#     length=len(lt)
#     for i in range(length-1):
#         for j in range(length-1-i):
#             if lt[j]>lt[j+1]:
#                 lt[j],lt[j+1]=lt[j+1],lt[j]
# bubbleSort(lt1)
# print('排序后：' + str(lt1))