#！/usr/bin/env python
# Author:Hank

'''
return关键字的使用:
1).结束函数

2).将结果返回给函数的调用者/调用处

【注意事项】
1).与return同一作用范围内的后面不要显示书写任何代码，因为永远不可能被执行到,不会报错。

2).return后面也可以不定义任何有效的数据，但是这样会将None值返回给调用处，一般没什么意义。
'''

def func1(a,b):
    print(a+b)
    #return后面也可以不定义任何有效的数据，但是这样会将None值返回给调用处，一般没什么意义
    return
    #在于return同一作用范围内的后面不要显示的书写任何代码，因为永远不可能被执行到，不会报错。
    # print('我被定义在return的后面...')

str1=func1(100,200)
print(str1,type(str1))

func1(50,60)