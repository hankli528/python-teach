'''
1.面向对象的三大特性：封装性、继承性、多态性

封装：

封装使用的领悟：

1).生活层面：食品、快递、计算机、明星...

2).计算机层面：

①.模块、类、函数...

②.属性数据的封装与隐藏

权限修饰符的概念：

public(公共的，范围最大) protected(收保护的)default(默认，缺省) private(私有的，范围最小)

python语言没有以上这些关键字：

对于python的属性私有化使用:__来实现

在设计完类，外界创建对象通过.的形式访问(设置)属性，

可能会出现跟现实情况不符的混乱数据，那么我们就将属性的设置权没收(外界不能直接通过.调用属性)，

在类的内部提供外界额外的访问方式(定义setter和getter方法)，

并且在需要的时候，可以在函数的内部加入数据合法性的校验；

模板：

对于setter函数，命名：set属性名(首字母大写)

对于getter函数，命名：get属性名(首字母大写)

私有属性：__age

设置值(__age)：

def setAge(self,age):

self.__age = age

获取值(__age)：

def getAge(self):

return self.__age
'''

'''
演示封装性的使用--->属性的封装与隐藏（私有化）
'''
class Person:
    def __init__(self,name,age,money):
        self.name=name
        self.__age=age
        self.__money=money

    '''
    提供外界额外的访问方式:getter和setter操作
    '''
    #设置值操作
    def setAge(self,age):
        #对age的内容进行合法性的校验
        if age<0 or age>130:
            print('年龄赋值有误...')
            raise Exception('年龄有误...')
        else:
            self.__age=age

    #获取值操作
    def getAge(self):
        return self.__age

    def setMoney(self,money):
        #...
        self.__money=money

    def getMoney(self):
        return self.__money

#实例化Person对象
p=Person('老王',30,30000)
# print(p.name,p.age,p.money)


'''
对象实例化之后，可能会对属性进行再次的访问(赋值、获取值)，

但是在外界直接通过对象.属性名的方式进行操作，很有可能造成数据与现实逻辑不符合的情况(脏数据)，

我们是需要避免的，那么该怎么办呢？

我们就将对象访问属性的行为没收(限制)，可以在需要的属性前定义__来实现私有化

之后可以提供外界额外的访问方式：一套getter和setter函数即可
'''

# p.age=-30
# print(p.age)

'''
以下操作并不是尝试修改私有属性，而且为对象动态添加属性的行为
'''
# p.__age=-30
# print(p.__age)


'''
__dict__属性：

作用：返回对象的属性名(键)，属性值(value)，以字典形式返回

从中我们可以看出，被所谓私有化的属性其实就是换了个名字(伪私有)，

命名的规则：_类名__属性名，

虽然我们也是可以在外界去访问它，但是一般人都不这么干(帅的人)
'''
print(p.__dict__)
p._Person_age=100
print(p.__dict__)

p.setAge(-100)
print(p.getAge())
print(p.__dict__)