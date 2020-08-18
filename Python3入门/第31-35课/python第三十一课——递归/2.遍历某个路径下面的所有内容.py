#！/usr/bin/env python
# Author:Hank

import os
'''
需求：遍历某个路径下面的所有内容（文件和目录，多层级的）
'''
#自定义函数(递归函数)：遍历目录层级（多级）
def printDirs(path):
    dirs=os.listdir(path)

    #循环处理列表
    for d in dirs:
        #组装d得到其绝对路径
        fileAbsPath=os.path.join(path,d)

        #判断是目录还是文件
        #如果是文件直接打印,如果是目录再次调用此函数
        if os.path.isfile((fileAbsPath)):
            print(d)
        elif os.path.isdir(fileAbsPath):
            print(d)
            printDirs(fileAbsPath)

path=r'F:\PyCharm\多味红豆\python第三十一课——递归\a'
printDirs(path)