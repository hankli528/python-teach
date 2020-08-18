#！/usr/bin/env python
# Author:Hank
'''
输入三个数，分别为小时、分钟、秒，然后输出下一个时刻

23 59 59

00:00:00

12 12 12

12 12 13

下面代码中最后的cls是清屏操作，在编译器中可能会没有效果
'''
import time
import os

hour=int(input('请输入小时:'))
minute=int(input('请输入分钟：'))
seconds=int(input('请输入秒钟：'))

#先进行数据校验
if (hour<0 or hour>24)or(minute<0 or minute>60)or(seconds<0 or seconds>60):
    print('请输入的时间有误，程序终止！')
    exit()

#如果程序执行到此处，说明接受的数据没有问题
while 1:
    seconds += 1
    if seconds == 60:
        seconds = 0
        minute +=1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == 24:
        hour = 0
        os.system('cls')

    print('%02d:%02d:%02d' %(hour,minute,seconds))
    time.sleep(0.5)
