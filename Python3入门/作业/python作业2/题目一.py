#！/usr/bin/env python
# Author:Hank
'''
实现99乘法表

显示效果如下：
1*1=1
1*2=2 2*2=4
1*3=3 2*3=6 3*3=9
···
1*9=9 2*9=18 3*9=27 ··· 9*9=81

'''
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,i*j),end=' ')
    print()