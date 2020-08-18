#！/usr/bin/env python
# Author:Hank

'''
演示：简单递归函数的定义和使用
'''
#需求：1~5进行累加
'''
找寻关系：
函数名：mySum(num)
    1).找临界点：运算到1（加到1）就结束了
    2).
    第一次:5+mySum(5-1)-->return 5+10
    第二次:4+mySum(4-1)-->return 4+6 10
    第三次:3+mySum(3-1)-->return 3+3 6
    第四次:2+mySum(2-1)-->return 2+1 3
    第五次:1           -->return 1
'''
def mySum(num):
    if num==1:
        return 1
    return num+mySum(num-1)
print(mySum(5))

#需求：计算1~5的阶乘
def jiechen(num):
    if num==1:
        return 1
    return num*jiechen(num-1)
print(jiechen(5))