#！/usr/bin/env python
# Author:Hank
'''
队列：满足特点 --> 先进先出，类似于我们生活中的买票、安检

【注意】

对于队列而言：python中有为其封装特定的函数，在collections模块中的deque函数就可以获取一个队列对象;

操作步骤：

步骤一：导入collections模块

步骤二：collections.deque() --> 返回队列对象

步骤三：使用队列对象调用其存和取的函数，完成需求
'''

'''
演示队列存取数据的特点：先进先出
'''
# import collections
#
# #获取队列对象：deque()
# queue=collections.deque()
# print(queue,type(queue))
#
# #向队列中逾加数据：进队操作
# queue.append('A')
# print(queue)
#
# queue.append('B')
# print(queue)
#
# queue.append('C')
# print(queue)
#
#
# #将队列中的数据弹出：出队操作
# obj=queue.popleft()
# print('弹出：'+obj)
#
# obj=queue.popleft()
# print('弹出：'+obj)
#
# obj=queue.popleft()
# print('弹出：'+obj)


'''
模拟使用队列结构实现遍历目录之广度遍历
'''
import collections,os
#自定义函数：实现遍历多目录层级操作(广度遍历)
def getAllFileQU(path):
    #获取一个队列
    queue=collections.deque()
    #将path数据进队
    queue.append(path)
    #只要queue中还有数据，循环就继续
    while len(queue)!=0:
        file_path=queue.popleft()
        #获取file_path中所有字内容(文件、子目录)
        files_list=os.listdir(file_path)
        #循环处理file_list中的每一个元素
        for file in files_list:
            #还原其绝对路径值
            fileAbsPath=os.path.join(file_path,file)
            #判断是文件还是目录，操作和深度遍历一样
            if os.path.isfile(fileAbsPath):
                print('文件：'+file)
            else:
                print('目录：'+file)
                queue.append(fileAbsPath)

# path=r'test.txt'
# getAllFileQU(path)

'''
为了更好的理解栈和列队存取数据的特点：

我们书写了深度遍历和广度遍历的代码操作，

从中得知不使用递归操作也可以使用遍历多层级目录的需求，

这样做的好处是：更加的节省内存资源
'''