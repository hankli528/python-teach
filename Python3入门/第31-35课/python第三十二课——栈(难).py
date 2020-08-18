#！/usr/bin/env python
# Author:Hank
'''
栈：满足特点 --> 先进后出，类似于我们生活中的子弹夹

【注意】

对于栈结构而言：python中没有为其封装特定的函数，我们可以使用list(列表)来模拟栈的特点
'''

'''
使用list对象来模拟栈结构存取数据的特点:先进后出
'''
# 定义一个列表对象,stack(变量名、引用名)
stack=[]

# 向栈中添加数据(模拟压栈)
# stack.append('A')
# print(stack)
#
# stack.append('B')
# print(stack)
#
# stack.append('C')
# print(stack)


# 将栈中的数据弹出(模拟弹出)
# obj=stack.pop()
# print('弹出：'+obj)
#
# obj=stack.pop()
# print('弹出：'+obj)
#
# obj=stack.pop()
# print('弹出：'+obj)



'''
模拟栈结构特点实现目录遍历之深度遍历
'''
import os

#自定义函数：实现深度遍历目录层级的操作
def getAllFileST(path):
    #定义一个列表
    lt=[]
    #将path(字符串、绝对路径)压栈
    lt.append(path)
    #根据lt的长度来决定循环执行的次数
    while len(lt)!=0:
        #将lt中的数据弹栈
        file_path=lt.pop()
        #得到file_path中的字内容(文件、子目录)以列表的形式返回
        file_list=os.listdir(file_path)
        #循环处理file_list
        for file in file_list:
            #将其中的每个元素还原成为绝对路径值
            fileAbsPath=os.path.join(file_path,file)

            '''
            判断是文件还是目录？
            如果是文件，直接打印其文件名即可
            如果是目录，先打印其目录然后在将其压栈
            '''
            if os.path.isfile(fileAbsPath):
                print('文件：'+file)
            else:
                print('目录：'+file)
                lt.append(fileAbsPath)

p=r'F:\PyCharm\多味红豆\python第三十一课——递归\a.txt'
getAllFileST(p)