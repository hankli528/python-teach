#！/usr/bin/env python
# Author:Hank
'''
3.模块(m)

概念：在python中.py结尾的文件，我们就称为模块，可以将类、函数、属性...等内容定义在模块中

分类:

1).标准库模块：安装完python环境就有的模块，这些模块都是最常用的模块；

例如：random、os、os.path、math、...

2).第三方模块：别人写的有价值的代码(面向全世界)，我们如果需要使用，

只需要通过pip安装即可

3).自定义模块：在项目开发过程中，团队中程序员自己定义的，可以给自己，也可以给别人调用

导入模块：

1).精确导入：

举例：

import time

from random import randint

2).模糊导入：

举例：

from math import *

from os import *

给导入的模块或者其函数、属性起别名：

使用as关键字来实现

【注意】：

一旦起了别名，之前的名字就不能用了

自定义模块：

需要先显示的导入自定义模块到当前模块中，然后就可以随意的使用其中的内容

代码if __name__ == __main__：此代码的作用是将不想被加载的代码定义其中

"包"的概念：package

创建一个python package，就是创建一个python的包，

包的作用：将多个有关联的模块纳入其中，方便之后的维护和管理

对于__init__.py和__pycache__目录，我们不需要关注它，但是不要删除它

第三方模块：

打开cmd --> 输入pip -V(此操作查看是否安装完成pip)

涉及的主要操作如下：

1).查看当前安装的所有第三方模块：pip list

2).查看某个第三方模块的详细信息：pip show 模块名

3).安装某个第三方模块：pip install 模块名例如：pip install redis

4).删除某个第三方模块：pip uninstall 模块名例如：pip uninstall redis
'''
import random
from random import shuffle
from math import pi,e
from time import *
from random import randint as r
import os as f

# import func
# from func import my_sum

'''
演示标准库模块的导入
'''
# print(random.randint(1,3))

lt=[1,2,3,4,5,6]

shuffle(lt)
# print(lt)
# print(pi,e)
#
# print('我睡了...')
#
# sleep(2)
#
# print('我醒了...')
#
# print(r(5,10))


'''
如果一旦给模块或者函数起了别名，原本的名字就不可以用了；
所以一下代码会报错
'''
# print(randint(3,7))
# print(f.getcwd())
# print(func.my_sum(10,20))
# print(func.my_max(10,20))
# print(my_sum(100,200))
