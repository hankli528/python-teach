#！/usr/bin/env python
# Author:Hank

'''
1.for...in循环：

有两个使用场景：

场景一：for in和range对象配合使用

range对象的引入讲解

格式：range([start,end,step])：

特点：索引满足含头不含尾的特点-->闭开区间

以上三个参数：start、end、step的含义和str切片一样理解

惰性序列对象：

将多个数据存入到容器对象中，直接通过print()函数打印其变量名，看到的数据内部信息不明确；
案例一：
'''
r=range(1,11)
# r=range(11)

#range对象可以理解为惰性序列对象(直接打印变量名看不清里面具体内容)
# print(r,type(r),len(r))


'''
range对象配合for in循环使用：

遍历的思想：
遍历：经过、经历、从头到尾走一遍
'''
# for i in r:
#     print(i,end=' ')
#
# print()
#
# for i in range(0,10,2):
#     print(i,end=' ')
#
# print()


'''
range为惰性序列对象，那么我们可以将其转换为非惰性序列对象！！

例如：

将range(1,6)对象转换为list对象

代码如下：
'''
lt = list(range(1,6))
# print(lt,type(lt),len(lt))

#遍历lt对象
# for j in lt:
#     print(j)



'''
场景二：for in和容器对象(str、list、tuple、set、dict)配合使用

#方式一：通过键找到值

for k in dic:

print(k + '-->' + str(dic.get(k)))

#方式二：直接先得到一个dict_items对象(此对象中有key和value并且存入到一个元祖中保存，对象每个元素都是元祖)

its = dic.items()

print(its,type(its),len(its))

for k,v in dic.items():

print(k,v)

总结：for in循环也可以和break&continue，以及else语句一起配合使用
'''

#案例二：
#演示for in 和容器对象(str,list,tuple,set,dict)配合使用
lt=['aa','bb','cc','dd']
'''
案例体会：
for...in循环中没有使用索引的思想，而while循环中一般会用到索引去访问容器中的元素内容
'''

#遍历lt对象，打印内容到控制台
# for i in lt:
#     #print(i)
#     i+='r'
# print(lt)
# print()
#
# lt1=['aa','bb','cc','dd']
# i=0
# while i<len(lt1):
#     # print(lt[i])
#     lt1[i] += 'r'
#     i+=1
# print(lt1)
# print()
#
# str1='abcdefg1234567'
# for i in str1:
#     print(i,end=' ')
# print()


'''
使用for in或者while循环遍历dic对象，打印键值对的内容
'''
dic={'name':'abc','age':25,'sex':'男'}
#方式一：通过键找到值
# for k in dic:
#     print(k+'--->'+str(dic.get(k)))


'''
#方式二：直接先得到一个dict_items对象
(此对象中有key和value并且存入到一个元祖中保存，
对象每个元素都是元祖)
'''
# its=dic.items()
# print(its,type(its),len(its))
#
# for k,v in dic.items():
#     print(k,v)


#案例三：
'''
演示for in循环配合break&continue和else语句配合使用
'''
#需求：遍历1~100的偶数，打印个数和总和-->使用for in实现
count=0
sum1=0
for i in range(1,101):
    if i%2 ==1:
        continue
    count+=1
    sum1+=i
    # print(i)
# print('偶数的个数为:%d' %count)
# print('偶数的总和为：%d' %sum1)

for i in range(1,11):
    if i==4:
        # break
        continue
    print(i)
else:
    print('如果没有碰到牛逼的break,我就会被执行...')