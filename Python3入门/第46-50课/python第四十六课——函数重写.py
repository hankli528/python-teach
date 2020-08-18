'''
3.函数重写(override)

前提：必须有继承性

原因：

父类中的功能(函数)，子类需要用，但是父类中函数的函数体内容和我现在要执行的逻辑还不相符

那么可以将函数名保留(功能还是此功能)，但是将函数体重构；

注意：

子类重写父类的函数，除了函数体以外的部分，直接复制父类的即可
'''

'''
演示函数重写的使用以及格式：
'''

# class Fu:
#     def test(self):
#         print('九阳神功...')
#
# class Zi(Fu):
#     def test(self):
#         print('九阳神功...')
#         super().test()
#         print('乾坤大挪移...')
#
# #实例化子类对象
# zi = Zi()
# zi.test()



'''
巩固函数重写的使用：

案例：描述新手机和旧手机之间的一些关系
'''
#定义旧手机类
class OldPhone:
    #打电话:
    def call(self,name,msg):
        print('正在给%s打电话，内容为：%s' % (name,msg))

    #发短信：
    def sendMSG(self,name,msg):
        print('正在给%s发短信，内容为：%s' % (name,msg))

#定义新手机类
class NewPhone(OldPhone):
    # 打电话:
    def call(self, name, msg):
        print('显示归属地和大头贴')

    # 发短信：
    def sendMSG(self, name, msg):
        super().sendMSG(name,msg)
        print('正在发送表情包...')

#实例化子类对象:
np=NewPhone()
np.call('苍老师','约吗？')
np.sendMSG('小泽老师','么么哒！！')
