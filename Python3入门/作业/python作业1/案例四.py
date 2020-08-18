#！/usr/bin/env python
# Author:Hank

'''
模拟实现用户登录，先验证用户名，只有用户名正确的才去验证密码；
一旦用户名和密码全部正确了，登录成功；
'''

# 定义用户名和密码
# username='abc'
# password='123'
#
# 从键盘输入用户名和密码
# input_user=input('请输入用户名：')
#
# if input_user==username:
#
#     #验证密码
#     input_pwd=input('请输入密码：')
#     if input_pwd==password:
#         print('登录成功...')
#     else:
#         print('密码错误,登录失败...')
# else:
#     print('用户名错误,登录失败...')


'''
加大难度，如果3次输入错误,则账号被锁定
'''
user_name=input('请输入用户名：')
if user_name == 'hank':
    print('用户名验证成功！')
    i=1
    while i <= 3:
        pass_word=input('请输入密码：')
        if pass_word=='123':
            print('恭喜密码输入正确，现已登录成功！')
            break
        else:
            if i==3:
                break
        print('密码输入有误，有3次输入机会,请重新输入...')
        i+=1
else:
    print('用户名输入错误,请再次输入...')