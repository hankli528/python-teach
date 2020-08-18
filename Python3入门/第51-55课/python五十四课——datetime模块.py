'''
3.datetime模块：
理解：datetime可以认为是time模块的补充/扩展
datetime模块中有一些常用类：
datetime类：记录了日期和时间数据信息
date类：记录了日期数据信息
time类：记录了时间数据信息

datetime类：
now()和today():获取当前的日期和时间对象(返回值的类型为：datetime)
utcnow():获取当前的日期和时间对象(utc时间，返回值的类型为：datetime)
'''
import datetime
dt=datetime.datetime.now()
# print(dt,type(dt))

dt1=datetime.datetime.today()
# print(dt1,type(dt1))

dt2=datetime.datetime.utcnow()
# print(dt2,type(dt2))

#***********#

#获取指定的日期和时间对象(类型：datetime)
#构造函数：date(,,,,)
dt3=datetime.datetime(2018,11,19,15,33,42,345678)
# print(dt3,type(dt3))

#将datetime类型对象转换为指定模式字符串
#strftime(fmt)
str1=dt3.strftime('%Y-%m-%d %X')
# print(str1,type(str1))

#从日期对象中分离出日期对象或者时间对象
#date() --> 得到date对象、time() --> 得到time对象
# print(dt3.date(),type(dt3.date()))
# print(dt3.time(),type(dt3.time()))

#从日期时间对象中得到对应的时间戳对象
#timestamp()
ts=dt3.timestamp()
# print(ts,type(ts))

#从日期时间对象得到对应的本地元组对象（类型是time模块下的struct_time类型）
#timetuple()
tp=dt3.timetuple()
# print(tp,type(tp))

'''
属性:
year,month,day,hour,minute,second,microsecond

fromtimestamp(ts):将时间戳对象转换为日期对象

timedelta类型：

timedelta([days=,hours=,minutes=,seconds=])：可以在不转换datetime类型数据的前提下进行相关的算数运算(日、分钟、秒钟...)
'''

'''
操作属性:
尝试获取日期时间对象中单独的年、月、日、时、分、秒、小数点后的数据
【注意】以下的操作不是针对函数调用，而是对于属性进行调用
'''
# print(dt3.year,dt3.month,dt3.day,dt3.hour,dt3.minute,dt3.second,dt3.microsecond)

#将时间戳对象转换为日期对象
d=datetime.date.fromtimestamp(ts)
# print(d,type(d))

#timedelta():可以在不转换datetime类型数据的前提下进行相关的算术运算(日、分钟、秒钟...)
delta=datetime.timedelta(days=1,hours=1,minutes=1,seconds=1)
print(delta,type(delta))

#计算时间差
obj=dt3-delta
print(obj,type(obj))
print(dt3+delta)


