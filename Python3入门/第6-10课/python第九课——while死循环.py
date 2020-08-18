'''
2.3.无限循环/死循环：

何时发生无限循环？

循环条件永远为True，就出现了无限循环

【注意】

无限循环是需要避免的，因为它极其占用系统资源；

但是配合我们之后讲的break等关键字，就会变得更有意义；

格式：

while True:

代码块
'''
#演示while的无限循环格式：

import time
while True:
    time.sleep(1)
    print('老郭真棒！萌萌哒...')

    while 1:
        #底层隐式的操作：bool(1)
        time.sleep(1)
        print('死啦！死啦...')

i = 1
i = []
if i: #底层隐式的操作：bool(1)
 print('是真的...')
else:
 print('是假的...')