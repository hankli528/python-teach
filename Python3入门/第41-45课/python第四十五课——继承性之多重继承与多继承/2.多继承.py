from child import Child

'''
测试模块

演示多继承的结构和使用：

子类：Child

直接父类(多个)：Father、Mother

注意：

由于有多个直接父类，多个父类都要自己给其属性赋值，

避免混淆，我们使用类名.__init__(...)这样格式的构造调用
'''
c = Child(100000000,'漂亮','python')
print(c.money,c.faceValue,c.work)
c.playing()
c.shopping()
c.smoking()