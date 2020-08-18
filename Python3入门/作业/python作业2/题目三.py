#！/usr/bin/env python
# Author:Hank
'''
模拟斗地主（超级简化版）
'''
import random

#1.准备牌环节
#存牌容器
pokerList=[]

#发牌后
pokerDict={}

#定义numList和colorList用于存储花色和点数
numList=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
colorList=['♠','♥','♦','♣']

for i in numList:
    for j in colorList:
        pokerList.append(j+i)

#额外加入大小王
pokerList.append('小王')
pokerList.append('大王')

#阶段测试
# print(pokerList)
# print(len(pokerList))

#2.选派环节
random.shuffle(pokerList)

#阶段测试
# print(pokerList)

#3.发牌环节
#准备4个容器用于存放3个玩家和底牌：player1、player2、player3、secretPai
player1=[]
player2=[]
player3=[]
secretPai=[]

#4.循环发牌，先将索引0,1,2发给底牌，然后将3发给玩家即可
i=0
while i<len(pokerList):
    if i>= 0 and i <= 2:
        secretPai.append(pokerList[i])
    elif i % 3 == 0:
        player1.append(pokerList[i])
    elif i % 3 == 1:
        player2.append(pokerList[i])
    else:
        player3.append(pokerList[i])
    i+=1

#5.看牌环节(封装函数)
def lookPai(lt):
    for i in lt:
        print(i,end=' ')
    print()

lookPai(player1)
lookPai(player2)
lookPai(player3)
lookPai(secretPai)