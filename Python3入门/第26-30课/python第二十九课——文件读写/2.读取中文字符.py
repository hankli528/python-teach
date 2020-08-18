#！/usr/bin/env python
# Author:Hank

'''
演示：读取中文字符

结论：
    1).如果不设置encoding,默认使用gbk进行编解码
    2).如果编码和解码不一致,最终导致报错,但是一旦设置了errors='ingore',那么就不会报错，而采取乱码现象显示
    3).tell():返回的是文件描述符的字节位
    4).对于读操作，必须保证路径中的文件一定是真实存在的，否则报错:FileNotFoundError
'''

#打开文件：
f2=open(r'F:\PyCharm\多味红豆\python第二十九课——文件读写\a.txt','r',encoding='gbk',errors='ignore')

#读取数据：
content2=f2.read()
print(content2)
print(f2.tell())
f2.seek(7)
content2=f2.read()
print(content2)

#关闭文件
f2.close()