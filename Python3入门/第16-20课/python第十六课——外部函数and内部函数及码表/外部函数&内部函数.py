#！/usr/bin/env python
# Author:Hank
'''
1.外部函数&内部函数

内部函数：

定义在某个函数的内部，就是内部函数；

【注意事项】：

1).内部函数可以随意使用它外部函数中的内容

2).外部函数不能使用内部函数中的内容

3).内部函数不能直接在外界被调用(与作用域有关)

4).内部函数的执行需要依赖于外部函数

nonlocal关键字：

如果想要在内部函数中修改其外部函数中变量的值，

可以先使用nonlocal定位到某个变量，然后重新赋值即可--> 例如：nonlocal aa = 30
'''
'''
演示外部函数和内部函数的结构关系，
演示他们的调用执行过程
'''
#定义外部函数outer()
def outer():
    #外部函数的变量a,赋值为10
    a=10
    print('outer1....')

    #定义内部函数inner()
    def inner():
        '''
        思考：内部函数可不可以使用外部函数的变量a?
        可以的
        '''
        print('inner:%d' % a)
        print('inner...')

        #定义内部函数变量b,赋值为20
        b=20

    #在当前的外部函数中启动内部函数
    inner()
    print('outer2...')
    '''
        思考：外部函数可不可以使用内部函数的变量b?
        不可以
    '''
    # print(b)

    def inner1():
        '''
            思考：内部函数可不可以修改外部函数中的变量a的值为20？
            可以的，使用nonlocal关键字来实现，原理和golbal一致
        '''
        nonlocal a
        a=20
        print(a)
    inner1()
    print('outer:%d' %a)

#调用外部函数，间接也执行内部函数
# outer()

'''
内部函数不能直接在外界被调用，一定是需要在它所作用的外部函数中被调用，
执行也是要外部函数的执行
'''

'''
强化内部函数和外部函数的知识点：
'''
a=100
def outer():
    a=10
    def inner():
        a=20
        print('我是inner...')
        print('a=%d' % a)
        def litter():
            a=30
            print('我是litter...')
            print('a=%d' % a)
        litter()
    inner()
    print('我是outer...')
    print('a=%d' % a)

#执行外部函数outer()
outer()