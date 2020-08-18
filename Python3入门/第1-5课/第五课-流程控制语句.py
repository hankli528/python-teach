'''
流程控制语句：

分类：

1).顺序结构

2).判断结构解析：如果...否则...

3).循环结构

1.判断结构：

格式分类：三种格式

格式一：

①

if 条件表达式:

语句块

②

执行流程：

计算机会先执行①，遇到了if关键字会执行条件表达式，

如果条件表达式的结果为True，那么就会立即进入到if的内部去执行语句块，

等到语句块执行完毕了，就可以认为if结构结束了，但是程序一定会去执行②

如果条件表达式的结果为False，那么就会不会进入到if的内部去执行语句块，

也就意味着if结构已经结束了，但是程序一定会去执行②

#需求：从键盘读入一个正整数，判断其奇偶性
num = int(input('请输入一个正整数：'))
if num % 2 == 0:
print('是偶数...')
if num % 2 == 1:
print('是奇数...')
print('程序结束了...')

格式二：

①

if 条件表达式:

语句块1

else:

语句块2

②

执行流程：

计算机会先执行①，遇到了if关键字会先执行条件表达式，

如果条件表达式的结果为True，那么就会立即进入到if的内部去执行语句块1，

等到语句块1执行完毕了，整个if...else结构就结束了，但是程序一定会去执行②

如果条件表达式的结果为False，那么就会立即进入到else的内部去执行语句块2，

等到语句块2执行完毕了，整个if...else结构就结束了，但是程序一定会去执行②
'''

'''
演示if第二种格式的使用：if...else...
'''
age = 21
if age > 18:
 print('恭喜你，成年了...')
else:
 print('对不起，你还不能看成人电影...')
print('但是你可以到老郭家里看...')
'''
使用判断结构if...else重构之前三元中的案例：两个数中的较大值
'''
num1 = 10
num2 = 20
if num1 > num2:
 print('较大值为：{}'.format(num1))
else:
 print('较大值为：{}'.format(num2))
'''
需求：
模拟一个购物系统，通过键盘输入：单价，数量，付款金额；
最后计算得到应收金额和找零；
单价：price
数量：amount
支付金额：money
总金额：totalPrice
找零：change
附加需求：
满500元打8折
'''
price = float(input('请输入单价：(￥)'))
amount = int(input('请输入数量：(件)'))
#计算得到总金额
totalPrice = price * amount
print('您本次一共消费：%s元' %totalPrice)
money = float(input('请输入付款金额：(￥)'))
#判断付款金额是否大于等于总金额
if money >= totalPrice:
 #金额足够，计算找零
 change = money - totalPrice
 print('收您：%s元，找零为：%s' %(totalPrice,money,change))
else:
 print('您支付的金额有误！请重新支付...')
