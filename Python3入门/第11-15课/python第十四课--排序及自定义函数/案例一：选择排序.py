#！/usr/bin/env python
# Author:Hank

# 案例一：选择排序
# 使用选择排序的思想实现列表数据的升序排序
lt=[45,12,56,-32,-3,44,75,-22,100]
length=len(lt)
# print('排序前：'+str(lt))

#使用嵌套循环来实现
#外层循环控制轮数，i可以认为是选中空间或者点
for i in range(0,length-1):
    #内层循环呢控制每一轮执行的次数，j可以认为是比较空间或箭头
    for j in range(i+1,length):
        #判断两空间中的内容，如果选中空间比比较空间中的数据大，则交换数据
        if lt[i]>lt[j]:
            #temp=lt[i]
            #lt[i]=lt[j]
            #lt[j]=temp
            lt[i],lt[j]=lt[j],lt[i]
# print('排序后：'+str(lt))