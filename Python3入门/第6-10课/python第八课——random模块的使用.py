'''
2.2.如何获取随机整数值？

引入random模块的使用

randint(a,b)函数：作用：返回给程序一个[a,b]范围内的随机整数注意：含头含尾闭区间

思路步骤：

第一步：导入random模块到相应的.py文件中 import random

第二步：通过random模块名调用randint(a,b)执行得到随机整数 random.randint(1,5)
'''

#案例1：
#演示random模块中randint函数的使用
import random
print("随机的整数为：%d" %random.randint(1,5))

#案例2：
#需求：完成10次加法测试，并输出得分
import random
print('10次加法测试即将开始，请准备!!')
#定义变量score记录得分
score = 0
#使用while循环来进行出题以及答题等操作，注意：10次
i = 1
while i <= 10:
    #生成两个[1,100]之间的随机整数
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)

    #定义变量answer记录正确的答案
    answer = num1 + num2

    #开始出题
    print("%d).%d + %d = ?(退出：-1)" %(i,num1,num2))

    #得到用户从键盘输入的结果 --> 变量user_answer
    user_answer = int(input())

    #判断用户输入的答案和正确答案是否一致
    if user_answer == answer:
        #说明答对了，给与正向鼓励，并且得10分
        print('答对了，你真棒！')
        score += 10
    elif user_answer == -1:
        print('太遗憾了，下次再挑战吧！')
        break
    else:
        print('答错了，你真笨！')
    i += 1
else:
    #将最终得分在控制塔打印显示
    print('10次加法测试已经结束，最终得分为：%d' %score)