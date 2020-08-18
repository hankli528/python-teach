#！/usr/bin/env python
# Author:Hank
'''
打印所有的水仙花数
水仙花数：满足两点：
1).必须是一个三位数(100~999)
2).个位数的立方 + 十位数的立方 + 百位数的立方 = 这个三位数本身
'''

i=100
while i<999:
    #分别得到个位、十位、百位的值
    gewei=i%10
    shiwei=i//10%10
    baiwei=i//100

    #判断
    if gewei ** 3 +shiwei **3 + baiwei**3 ==i:
        print('水仙花数为:{}'.format(i))
    i += 1

