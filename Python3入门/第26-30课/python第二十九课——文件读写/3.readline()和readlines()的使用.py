#！/usr/bin/env python
# Author:Hank

'''
演示readline()和readlines()的使用：
'''
#1.打开文件
f3=open(r'a.txt','r',encoding='gbk')

#2.读取数据
content3=f3.readline()
print(content3)

lines_list=f3.readlines()
print(lines_list)

#3.关闭文件
f3.close()
