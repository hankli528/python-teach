'''
while循环：

2.1.有四要素组成：

①.初始化条件(执行一次)一个起始数据/起点，一般使用变量来进行存储

②.循环条件(可能执行多次)循环合适结束全靠它，执行结果为True，那么循环继续，反之，循环就终止了

补充：需要和初始化条件配合

③.迭代条件(可能执行多次)用来改变初始化条件中的数据，只有变化了，才有终止的那一刻

④.循环体(可能执行多次)需要重复执行的逻辑代码

格式：

①

while ②:

④

③

⑤

执行流程：① -> ② -> ④ -> ③ -> ② -> ④ -> ③ -> ② -> ⑤

False
'''

#案例1：
#演示while循环的使用
#需求：打印10次马上有钱
# i = 0
# while i < 10:
#  print("马上有钱")
#  # i = i + 1
#  i += 1

 #案例2
 # 需求：打印1~100之间的偶数,并且得到偶数的个数和总和
 # 有计数和累加的思想 --> 可以定义变量来接受
 # count = 0  # count的作用是为了记录偶数的个数
 # sum1 = 0  # sum1的作用是为了记录偶数的总和
 # i = 1
 # while i < 101:
 #     if i % 2 == 0:
 #         print(i)
 #     count += 1
 #     sum1 += i
 #     i += 1
 # print('1~100之间偶数的个数为：%d' % count)
 # print('1~100之间偶数的总和为：%d' % sum1)

#案例3：
'''
需求：
打印1~150，
如果是3的倍数追加'foo'，
如果是5的倍数追加'biz'，
如果是7的倍数追加'baz'
效果如下：
1
2
3 foo
4
5 biz
6
7 baz

15 foo biz

105 foo biz baz

150 foo biz
'''
# i = 1
# while i <= 150:
#     print(i, end="")
#     if i % 3 == 0:
#         print(" foo", end="")
#     if i % 5 == 0:
#         print(" biz", end="")
#     if i % 7 == 0:
#         print(" baz", end="")
#     # 以下的print()的作用仅仅是为了换行
#     print()
#     i += 1
