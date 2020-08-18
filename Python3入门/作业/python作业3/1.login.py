#！/usr/bin/env python
# Author:Hank
'''
修改登录程序，只让输入密码错误的次数为3次，如果超过3次，就不让输入了
'''
username='abc'
password='123'

input_user=input('请输入用户名:')

#先验证用户名
if input_user==username:

    #再验证密码，3次机会
    i=3
    while i>0:
        input_pwd=input('请输入密码：')
        if input_pwd==password:
            print('登录成功...')
            break
        else:
            i -=1
            if i>0:
                print('密码输入有误，还有%d次尝试机会...' %i)
            else:
                print('密码输错次数超过3次，请10分钟后再尝试...')


else:
    print('用户名不存在,登录失败...')
