#！/usr/bin/env python
# Author:Hank
'''
自定义函数：实现文件复制操作
有形参（2个） 没有返回值
相似版（不用）
'''

def copyFile(src,dest):
    #1.打开两个文件：1个关联读操作，1个关联写操作
    fr=open(src,'rb')
    fw=open(dest,'wb')

    #读和写操作
    content=fr.read()
    fw.write(content)

    #关闭两个文件
    fw.close()
    fr.close()

def copyFile01(src,dest):
    #1.打开两个文件：1个关联读操作、1个关联写操作
    fr=open(src,'rb')
    fw=open(dest,'wb')

    #读和写操作
    while 1:
        content=fr.read(1024*1024)
        if not content:
            break
        else:
            fw.write(content)

    #关闭两个文件
    fw.close()
    fr.close()

src=r'F:\PyCharm\多味红豆\python第二十九课——文件读写\a.avi'
dest=r'F:\PyCharm\多味红豆\python第二十九课——文件读写\c.avi'

# copyFile()
# copyFile01()