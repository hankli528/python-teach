#！/usr/bin/env python
# Author:Hank

'''
1.性能：
py3.x起始比py2.x效率低，但是py3.x有极大的优化空间，效率正在追赶
'''

#************************************************#

'''
2.编码：
py3.x原码文件默认使用utf-8编码，使得变量名更为广阔
'''
中国='CHI'
print(中国) #结果为：CHI

#************************************************#

'''
3.语法：
3.1 去除了<>,改用!=
'''
'''
#python2
>>> 1<>2
True
>>> 1!=2
True
>>> 
'''
'''
#python3
>>> 1<>2
  File "<stdin>", line 1
    1<>2
      ^
SyntaxError: invalid syntax
>>> 1!=2
True
'''

'''
3.2 加入as和with关键字，还有True,False,None
'''

'''
3.3 整型触发返回浮点数，整除请使用//
'''
'''
#python2
>>> 5/3
1
>>> 5.0/3
1.6666666666666667
>>> 
'''

'''
#python3
>>> 5/3
1.6666666666666667
'''

'''
3.4 加入nonlocal语句
'''

'''
3.5 去除print语句，加入print()函数
'''
# py2.x
# print 'The answer is',2*2

#py3.x
# print('The answer is',2*2)


'''
3.6 去除了raw_input,加入input()函数
'''


'''
3.7 新的super(),可以不再给super()传参数
'''
class C(object):
    def __init__(self,a):
        print('C',a)
class D(C):
    def __init__(self,a):
        super().__init__(a) #无参数调用super()


'''
3.8 改变了顺序操作符的行为，例如x<y,当x和y类型不匹配时抛出
TypeError而不是返回随即的bool值
'''
'''
#python2
>>> 2<"4"
True
'''

'''
#python3
>>> 2<"4"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'int' and 'str'
'''


'''
3.9 新式的8进制字变量
'''
'''
#python2
>>> 0666
438
'''
'''
#python3
>>> 0666
  File "<stdin>", line 1
    0666
       ^
SyntaxError: invalid token
>>> 0o666
438
'''

#************************************************#

'''
4.字符串和字节串

python2:字符串以8-bit字符串存储

python3:字符串以16-bit Unicode字符串存储，
现在字符串只有str一种类型
'''

#************************************************#

'''
5.数据类型
5.1 Py3.x去除了long类型，现在只有一种类型--int,但它的行为就像2.x版本的long
'''
'''
5.2 新增了bytes类型，对应于2.x版本的八位串
>>> b=b'china'
>>> b
b'china'
>>> type(b)
<class 'bytes'>

str对象和bytes对象可以使用.encode()(str->bytes) or .decode()(bytes->str)方法相互转化
'''

#************************************************#

'''
6.面向对象
引入抽象基类
'''

#************************************************#

'''
7.异常
所有异常都从BaseException继承，并删除了StardardError
'''
'''
#python2
try:
    #....
except Exception,e:
    #....

#python3
try:
    #....
except Exception as e:
    #....
'''

#************************************************#

'''
8.其他
8.1 xrange()改名为range(),要想使用range()获得一个list,必须显调用
'''
'''
#python2
>>> list(xrange(5))
[0, 1, 2, 3, 4]
'''
'''
#python3
>>> list(range(5))
[0, 1, 2, 3, 4]
'''

'''
8.2 file类被废弃
'''
'''
#python2
>>> file
<type 'file'>

打开文件：
file(path)
open(path)
'''
'''
#python3
>>> file
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'file' is not defined

打开文件：
open(path)
'''

