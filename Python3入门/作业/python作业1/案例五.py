#！/usr/bin/env python
# Author:Hank
'''
从键盘读入10个整数，得到正数、负数和零的个数
'''
zs=0
fs=0
ling=0

i=1
while i<=5:
    num=int(input('请输入第%d个整数：' %i))

    if num<0:
        fs+=1
    elif num>0:
        zs+=1
    else:
        ling+=1

    i += 1

print('正数的个数为：' + str(zs))
print('负数的个数为：' + str(fs))
print('零的个数为：' + str(ling))