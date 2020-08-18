'''
1.time、datatime、calendar模块的引入讲解(重视)

Unix时间戳(timestamp)：返回的是数值类型数据(float值)，

概念：记录了从1970年00点00分00秒至今的秒数

UTC时间：世界协调时间

GMT时间：格林尼治时间

CCT时间：北京时间(当前时间)，属于东八区【注意】比UTC时间 + 8小时

2.time模块

clock()：打点操作，返回一个科学计数法得到的值(非常小)；作用：用于测试功能的性能

sleep(s)：休眠s秒，然后继续向下执行程序

time()：返回时间戳数据对象，类型为浮点型(float)

localtime(ts)：将时间戳数据转换为一个本地时间元祖对象(class为time_struct)返回
'''
import time
'''
演示time模块的使用：常用的函数
'''
#time():返回时间戳对象，数据类型是浮点型
ts=time.time()
# print(ts,type(ts))

#localtime(ts):将时间戳数据转为一个本地时间元组对象返回
#[注意]：返回的是time.struct_time类型的对象，内部维护着9个元素
b=time.localtime()
# print(b,type(b))

# time.sleep(2)

ts=time.time()
b=time.localtime(ts)
# print(b,type(b))

#gmtime(ts):将时间戳数据转换为一个utc时间元组对象(class为time_struct)返回
utc=time.gmtime()
# print(utc)
# time.sleep(2)
ts=time.time()
# print(time.gmtime(ts))


'''
#mktime(tp):将本地元组对象转换为时间戳对象
注意：mktime(tp)函数的调用执行，必须有一个实际参数的传入，参数类型为time.struct_time对象
返回值不会保留小数点后7位，只有一位（默认为0）
'''
tp=(2018,11,19,14,30,44,0,323,0)
ts=time.mktime(tp)
# print(ts,type(ts))

#asctime(tp):将本地元组对象转换为字符串数据(显示的样式是默认的)
#ctime(ts):
str2=time.ctime(ts)
# print(str2,type(str2))

#将本地时间元组对象转换为字符串数据
#asctime(tp)
str1=time.asctime(tp)
# print(str1,type(str1))

'''
将本地时间元组对象转换为字符串数据（自定义输出样式）
字符格式：
%Y:四位的年 相当于：yyyy

%y:两位的年 相当于：yy

%m:月份

%d:天数

%H：小时

%M：分钟

%S：秒钟

补充“
%h:月份（英文简写）

%D：格式 月/日/年（两位）

%X：格式 小时：分钟：秒钟
'''
#strftime(format,tp):将本地元组对象以（format格式化）为str类型的数据返回
# tp=(2018,11,19,14,30,44,0,323,0)
# str3 = time.strftime('%Y-%m-%d %H:%M:%S',tp)
# str3 = time.strftime('%y/%m/%d %H:%M:%S',tp)
# str3=time.strftime('%D %X',tp)
# print(str3)

#以下代码有问题：报错信息为：UnicodeEncodeError 原因格式内容不能有中文
# str3 = time.strftime('%Y"年"%m"月"%d"日" %H:%M:%S', tp)
# print(str3)


'''
strptime(str,format):将字符串数据以规定的format进行解析得到一个本地时间元组对象返回
【注意】：
解析字符串数据的时候格式（format）必须和字符串格式的这个format保持一致
'''
# tp=(2018,11,19,14,30,44,0,323,0)
# str3 = time.strftime('%Y-%m-%d %H:%M:%S',tp)
# tp1=time.strptime(str3,'%Y-%m-%d %H:%M:%S')
# print(tp1)

'''
以下代码会报错：ValueError
原因：解析字符串数据的时候格式（format）必须和字符串格式化的这个format保持一致
'''
# tp1 = time.strptime(str3,'%Y/%m/%d %H:%M:%S')
# print(tp1,type(tp1))

#clock():
c1=time.clock()
#返回一个科学计数法的浮点数据（非常小）
# print(c1)

# time.sleep(2)
c2=time.clock()
# print(c2)

# time.sleep(2)
c3=time.clock()
# print(c3)

