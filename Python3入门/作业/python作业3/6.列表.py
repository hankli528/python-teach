#！/usr/bin/env python
# Author:Hank
'''
需求1：生成一个数字列表，范围是3~11
'''
#不使用列表生成时
# print(list(range(3,12)))

#使用列表生成式
# print([x for x in range(3,12)])


'''
需求2：生成一个2*n+1的数字列表，n的取值范围为[2,8]
'''
#不使用列表生成式
# lt1=[]
# for i in range(2,9):
#     lt1.append(2*i+1)
# print(lt1)

#使用列表生成式
# print([2*n+1 for n in range(2,9)])

'''
需求3：[10,21,-9,0,-13,23,45,78,100],过滤掉小于20的那些数字，将满足的放入新列表
'''
# lt=[10,21,-9,0,-13,23,45,78,100]

# 不使用列表生成式
# lt2=[]
# for i in lt:
#     if i > 20:
#         lt2.append(i)
# print(lt2)
#
# 使用列表生成式
# print([x for x in lt if x >= 20])


'''
需求4：
将两个列表中的元素全排列，以元祖的形式放入一个新的列表中
L1 = ['苹果', '香蕉', '橙子']
L2 = ['牛奶', '果汁']
'''
# L1 = ['苹果', '香蕉', '橙子']
# L2 = ['牛奶', '果汁']

# 不使用列表生成式
# lt3=[]
# for i in L1:
#     for j in L2:
#         lt3.append((i,j))
# print(lt3)

# 使用列表生成式
# print([(x,y) for x in L1 for y in L2 ])

