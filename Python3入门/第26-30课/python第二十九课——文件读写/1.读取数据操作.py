#！/usr/bin/env python
# Author:Hank

# 演示读取数据操作：
path=r'a.txt'

# 1.打开文件
f1=open(path,'r')


# 2.读取数据
content1=f1.read(3)
print(content1)

content1=f1.read(6)
print(content1)

content1=f1.read()
print(content1)


# tell():
i=f1.tell()
print(i)

# seek()
f1.seek(5)
content1=f1.read()
print(content1)

# 3.关闭文件
f1.close()