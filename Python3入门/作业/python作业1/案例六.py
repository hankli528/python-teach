#！/usr/bin/env python
# Author:Hank
'''
完成猜数字游戏
'''
import random
print('欢迎来到数字游戏：（1-100之间，退出：-1）')

#随机得到一个需要猜测的整数
answer=random.randint(1,100)

#作弊
# print('数为：%d' % answer)

print('猜吧...')

while 1:
    user_answer = int(input())

    if user_answer==answer:
        print('恭喜你，猜对了')
        break
    elif user_answer == -1:
        print('太遗憾，下次玩吧...')
        break
    elif user_answer > answer:
        print('太大了，继续猜...')
    else:
        print('太小了，继续猜...')
