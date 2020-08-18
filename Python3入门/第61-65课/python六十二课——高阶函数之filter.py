import collections
'''
高阶函数之：
filter函数：过滤数据的，最终返回一个惰性序列对象(filter对象，迭代器对象)
解释：
filter的意思：在计算机领域中我们都称为过滤器
格式：
filter(fn,lsd)：
参数和map、reduce一样理解
功能：
将lsd中的每一个元素都给到fn函数
如果fn函数的返回值为True，那么就保留这个元素到filter对象中
如果fn函数的返回值为False，那么就舍弃这个元素，不会保留到filter对象中
最终filter函数执行完毕了，返回给程序一个filter对象(迭代器对象)
'''

#需求：lt=[1,2,3,4,5,6,7,8]-->效果：[2,4,6,8]
lt=[1,2,3,4,5,6,7,8]

#代码实现一：老技术
lt1=[]
for i in lt:
    if i%2==0:
        lt1.append(i)
# print(lt1)

#代码实现二：新技术
def func(obj):
    if obj%2==0:
        return True
    return False
fo=filter(func,lt)
# print(fo,type(fo))
# print(isinstance(fo,collections.Iterator))
# print(next(fo))
# print(list(fo))

#终极版
# print(list(filter(lambda x:x%2==0,lt)))



'''
需求：
lt = [123,'abcd',0,3.14,0.0,'haha','hehe','',True,False,(),[],{},[1,2,3],{11,22,33},{'name':'jack','age':23}]
得到效果如下：
[123,'abcd',3.14,'haha','hehe',True,[1,2,3],{11,22,33},{'name':'jack','age':23}]
'''
lt = [123,'abcd',0,3.14,0.0,'haha','hehe','',True,False,(),[],{},[1,2,3],{11,22,33},{'name':'jack','age':23}]
# print(list(filter(lambda x:bool(x),lt)))
# print(list(filter(bool,lt)))


'''
需求：
lt1 = ['aaaaaaaa','bbbb','cccccc','ddd']
得到效果如下：保留长度大于等于4的元素
['aaaaaaaa','bbbb','cccccc']
'''
lt1 = ['aaaaaaaa','bbbb','cccccc','ddd']
print(list(filter(lambda x:len(x) >= 4,lt1)))