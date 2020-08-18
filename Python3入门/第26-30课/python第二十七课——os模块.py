#！/usr/bin/env python
# Author:Hank

#演示os模块中常用的属性和函数:
'''
1.os模块：

作用：管理文件和目录

属性：

os.name：返回系统类型 常用的windows系统 --> nt

os.environ：返回当前系统所有的环境变量

os.environ.get(ver)：返回ver环境变量的内容
'''
import os
# print(os.name)
# print(os.environ,type(os.environ))
# print(os.environ.get('path'))


'''
函数：
以下函数如果需要传入path的，既可以是绝对路径也可以是相对路径

绝对路径：也称为完成路径，一串物理地址，带盘符的

相对路径：相对的概念，拿某一个位置作为参照物，得到的路径内容，不带盘符的

1、os.getcwd()：返回当前正在被执行的文件的绝对路径

os.listdir()：将当前路径下的所有文件和子目录以列表的形式返回
'''
# print(os.getcwd())
# print(os.listdir())


'''
2、os.mkdir(path)：创建单级目录，path既可以是绝对路径也可以是相对路径；【注意】如果目录已经存在，报错

os.makedirs(path)：创建多级目录，path既可以是绝对路径也可以是相对路径；【注意】如果目录已经存在，报错
'''
#如果路径下已经存在相同名字的目录，还要点击创建，会报错：FileExistsError
# os.mkdir(r'D:\python\day\hello')
# os.mkdir(r'aa')

'''
对于mkdir()而言：只能一次创建一层目录，不能级联创建目录，会报错：FileNotFoundError
'''
# os.mkdir('bb\cc\dd')
# os.makedirs('bb\cc\dd')

'''
makedirs()函数能不能只创建单级目录？
可以的
'''
# os.makedirs('bb\cc\dd')


'''
删除目录&文件：
【注意】：删除操作有风险，使用需谨慎，因为不走回收站...

删除目录：
os.rmdir(path)：删除单级目录，path既可以是绝对路径也可以是相对路径；【注意】如果目录已经不存在，报错
os.removedirs(path)：删除多级目录，path既可以是绝对路径也可以是相对路径；【注意】如果目录已经不存在，报错

删除文件：
remove(path):删除文件
'''
# os.rmdir(r'G:\aa\bb\cc\dd')
# os.rmdir(r'bb\cc\dd')

# os.removedirs(r'G:\aa\bb\cc')
# os.removedirs(r'bb\cc')

'''
rmdir()和removedirs()：只能删除目录，不能删除文件
'''
# os.rmdir(r'G:\aa\1.html')

# os.remove(r'G:\aa\2.html')

'''
remove()函数只能删除文件，不可删除目录（无效的），会报错：PermissionError
'''
# os.remove('bb\cc\dd')


'''
4、os.rename(old,new)：将old(原名)以new(新的名字)取代(重命名)
'''
# os.rename('abc','def')
# os.rename('demo.html','hello.html')


'''
演示path模块中常用的函数：

join(first,second):first和second两部分内容（字符串）拼接成为新的串（描述物理路径的）
【注意】不检测路径是否真实存在

5、os.system()：...

os.path.join(first，second)：将first和second组合以字符串的形式返回

os.path.getsize(path)：获取当前路径内容所对应的容量大小(字节量)
'''
import os

p=os.path.join(r'G:\aa',r'test.txt')
# p=os.path.join(r'G:\aa',r'test1.txt')
# print(p,type(p))

'''
getsize(path):返回path路径(内容：文件层面)所包含的字节里
'''
# print(os.path.getsize(r'G:\aa\test.txt'))
# print(os.path.getsize(r'G:\aa'))


'''
6、os.path.isfile(path)：判断path是否是一个文件，返回布尔值

os.path.isdir(path)：判断path是否是一个目录，返回布尔值

os.path.exists(path)：判断path是否真实存在，返回布尔值
'''
path=r'G:\aa\test.txt'
# print(os.path.exists(path))
# print(os.path.isfile(path))
# print(os.path.isdir(path))


'''
7、os.path.dirname(path)：将path中最后一个前面的部分以字符串返回

os.path.basename(path)：将path中最后一个后面的部分以字符串返回
'''
# path=r'G:\aa\test.txt'
# str1=os.path.dirname(path)
# print(str1)
# print(type(str1))

# str2=os.path.basename(path)
# print(str2)
# print(type(str2))


'''
8、os.path.split(path)：返回一个元素对象，将path内容中最后一个的前面部分放入到元祖的第一个元素中，

的后面部分放入到元祖的第二个元素中；

os.path.splitext(path)： 返回一个元素对象，将path内容中最后一个.的前面部分放入到元祖的第一个元素中，

.以及其后面部分放入到元祖的第二个元素
'''
path=r'G:\aa\test.txt'
tp=os.path.split(path)
# print(tp)
# print(type(tp))

tp1=os.path.splitext(path)
# print(tp1)
# print(type(tp1))