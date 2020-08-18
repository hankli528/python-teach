#！/usr/bin/env python
# Author:Hank
'''
演示：finlly语句的作用
'''
try:
    fr=""
    path=r'F:\PyCharm\多味红豆\第26-30课\python第三十课——异常\kaifanglist1.txt'
    fr=open(path,encoding='utf-8')
    print(fr.read())
except:
    print('处理啦，处理啦')
finally:
    print('我是finally,我里面的代码一定会被执行...')
    if fr:
        fr.close()


'''
演示finally的小案例：
'''
def func1():
    try:
        print('我是try...')
        print(10/0)
        return 1
    except:
        print('我是except...')
        return 2
    finally:
        print('我是finally...')
        return 3

num=func1()
print(num)