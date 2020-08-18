#！/usr/bin/env python
# Author:Hank
'''
自定义函数(列表对象)：求最大值、最小值、求和、平均值,调用执行看效果
'''
lt=[33,56,-3,46,22,-5,100,35,88]

def my_max(lt):
    #假设列表lt第一个元素是最大的
    max=lt[0]
    i=1
    while i< len(lt):
        if max < lt[i]:
            max=lt[i]
        i+=1
    return max
print('最大值为：%d' %(my_max(lt)))
print(my_max(lt))


def my_min(lt):
    min=lt[0]
    i=1
    while i< len(lt):
        if min > lt[i]:
            min=lt[i]
        i+=1
    return min
print('最小值为：%d' %(my_min(lt)))
print(my_min(lt))

#求和
def my_sum(lt):
    sum=0
    for i in lt:
        sum+=i
    return sum
print('求和为：%d'%(my_sum(lt)))
print(my_sum(lt))


#求平均
def my_avg(lt):
    return my_sum(lt)/len(lt)
print('平均值为：%d'%(my_avg(lt)))
print(my_avg(lt))