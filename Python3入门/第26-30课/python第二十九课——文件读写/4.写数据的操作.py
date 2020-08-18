#！/usr/bin/env python
# Author:Hank

'''
演示写数据的操作：

结论：往文件中写入数据，如果文件不存在，先创建文件，再写入内容
'''

#1.打开文件
fw=open(r'd.txt','w',encoding='utf-8')

#2.写数据操作
fw.write('李白威武霸气\n')

#以下操作出现了覆盖的情况
fw.write('hank is a shuaige')

#3.关闭文件
fw.close()

'''
文件一旦被close了，就不能再次执行相关函数的调用了，否则报错：
'''
# fw.write('nsdfasg')
fw=open(r'd.txt','w',encoding='utf-8')
fw.write('\n李白又回来了')
fw.close()