'''
2.4.time模块的初体验

sleep(sec)函数：程序一旦执行到sleep()函数，会立即休眠sec秒，等到时间到了，自动醒过来，然后继续往下执行...

思路步骤：

第一步：导入time模块 import time

第二步：time模块名调用sleep(sec)执行让程序休眠sec秒 time.sleep(5)

2.5.break&continue关键字

对于break关键字而言，在循环中一旦遇到了break关键字，立即结束当前循环

对于continue关键字而言，在循环中一旦遇到了continue关键字，立即结束当次循环，开始下一次循环

案例：
'''
#演示brak和continue关键字的使用:
# i=1
# while i<11:
#     if i==5:
#         i+=1
#         break
        #continue
        #和break continue在同一作用范围内，它们的后面不应该定义代码的代码，因为永远不可能被执行到。
        #i+=1
        # print(i)
        # i+=1
# print('-'*8)

'''
需求：打印1~100的奇数，个数和总和
使用continue关键字参与来实现
'''
# i=1
# while i<= 100:
#     if i%2==0:
#         i+=1
#         continue
#     print(i)
#     i+=1

'''
2.6.else语句配合循环使用

格式：

else:

语句块

【注意事项】

如果循环是正常终止，那么else中的语句块一定会被执行

如果循环是由于break关键字而终止，那么else中的语句块就不会被执行

案例:
'''
#演示else语句配合循环使用
i=1
while i<=10:
    if i==5:
        break
    print(i)
    i+=1
else:
    print('只要不碰到牛逼break，我就会被执行...')