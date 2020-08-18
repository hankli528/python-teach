#！/usr/bin/env python
# Author:Hank
'''
演示：
    1).异常处理的定义格式；
    2).常见的运行时异常类型；
'''
try:
    # print(10/0)
    num=int('132a')
# except Exception as e:
#     print('出错了...代码解决了')

# except:
#     print('我是Exception的简化版...')

# except ZeroDivisionError as e:
#     print(e)
    # pass

# except TypeError as e:
    # print('出现类型不匹配的异常了...')

# except ValueError as e:
#     print(e)

# except FileNotFoundError as e:
#     print('出现文件找不到的异常了...')

# except Exception as e:
#     print('出错了...代码解决了！！')

except (ZeroDivisionError,TypeError,ValueError,FileNotFoundError) as e:
    print('出现异常了...')

print('我会被执行吗？？')