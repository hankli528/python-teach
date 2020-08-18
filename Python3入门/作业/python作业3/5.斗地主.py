#！/usr/bin/env python
# Author:Hank

'''
实现斗地主优化（优化了可以在看牌是牌从小到大排列）
'''
import random

#1.准备牌
pokerList=[]
pokerDict={}
numList=['3','4','5','6','7','8','9','10','J','Q','K','A','2']
colorList=['♠','♥','♦','♣']

i=0
for x in numList:
    for y in colorList:
        pokerList.append(i)
        pokerDict[i]=y+x
        i += 1

#加入大小王
pokerDict[52]='小王'
pokerDict[53]='大王'
pokerList.append(52)
pokerList.append(53)


#测试
# print(len(pokerList))
# print(pokerList)
# print(pokerDict)

#2.洗牌
random.shuffle(pokerList)

#3.发牌
player1=[]
player2=[]
player3=[]
secretPai=[]

num=0
while num < len(pokerList):
    if num < 3:
        secretPai.append(pokerList[num])
    elif num%3 == 0:
        player1.append(pokerList[num])
    elif num%3 == 1:
        player2.append(pokerList[num])
    else:
        player3.append(pokerList[num])
    num += 1

#4.看牌
def lookPai(lt,dic):
    lt.sort()
    for i in lt:
        print(dic.get(i),end=' ')
    print()

print('player1')
lookPai(player1,pokerDict)
print('*******************')
print('player2')
lookPai(player2,pokerDict)
print('*******************')
print('player3')
lookPai(player3,pokerDict)
print('*******************')
print('secretPai')
lookPai(secretPai,pokerDict)