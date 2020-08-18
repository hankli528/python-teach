#！/usr/bin/env python
# Author:Hank
'''
演示with...as...操作
'''
path=r'F:\PyCharm\多味红豆\第26-30课\python第三十课——异常\kaifanglist1.txt'
with open(path,'r',encoding='utf-8') as fr:
    print(fr.read())
    
'''
注意事项：

1).将可能出现异常的代码定义到try语句中(try可以认为是扫描器)，

但是它是不具备处理异常的能力

2).一旦try中出现了异常对象(自动、手动)，第一个except会尝试去捕获它(捕获器)，

如果类型匹配，则捕获成功，对象即被处理，然后会顺势去执行except中的内容(逻辑代码)，

如果类型不匹配，则捕获失败，那么程序会继续去匹配下一个捕获器...

3).将一定需要被执行的代码放入到finally语句中，finally的特点：一定会被执行；

例如：关闭文件、关闭数据库连接...

4).with语句(python的语法糖)，可以帮助我们自动关闭文件

5).如果try中没有出现异常，那么else语句一定会被执行；反之，不会被执行

6).人为手动去抛出异常对象，使用raise关键字；格式：raise 异常类型(异常信息)

7).如果except后面定义的类型是Exception，那么此捕获器必须定义在最后位置(小的在前，大的在后)

8).except后面可以定义一个元祖对象，同时接受多个异常类型作为其元素，那么它就具有捕获多种异常类型对象的能力

9).except后面不定义任何异常类型，那么其可以认为是Exception的简化版

10).捕获器(except)不具备捕获处理语法错误这样的现象

11).常见的运行时异常类型：TypeError、IndexError、FileNotFoundError...

【注意】异常并没有学完，还有自定义异常类需要在面向对象学习过程中(继承学完)在进行讲解

总结：异常处理就主要学习掌握5个关键字：try、except、finally、else、raise
'''