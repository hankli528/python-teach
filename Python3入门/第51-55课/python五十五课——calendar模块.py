'''
4.calendar模块：

构造：calendar(year,[w=2,l=1,c=6])：返回year年的完整的日历信息对象

和闰年相关的函数如下：

isleap(year)：判断year是否是闰年

返回True，说明是闰年

返回False，说明不是闰年

leapdays(y1,y2)：返回[y1,y2)之间的闰年个数
'''
import calendar
'''
演示calendar(日历):模块的使用
'''
#构造：calendar(year,[w=2,l=1,c=6]):返回year年的完整的日历信息对象
c=calendar.calendar(2018)
# print(c)
# print(type(c))

'''
关于闰年的一些方法：
issleap(year):判断year是否是闰年
返回True,说明是闰年
返回False,说明不是闰年
'''

# print(calendar.isleap(2004)) #True 是闰年
# print(calendar.isleap(2018)) #False 不是闰年 是平年

'''
leapdays(y1,y2):返回[y1,y2]之间的闰年个数
'''
# print(calendar.leapdays(2010,2018))


#month(year,month):返回year年month月的日历信息对象
print(calendar.month(2018,12))

'''
monthrange(year,month)：返回一个元祖对象，一共有两个元素
第一个元素存储的是1号是本周的第几天，
第二个元素存储的是本月一共有几天
'''
print(calendar.monthrange(2018,12))

#timegm(tp):将时间元组对象转换为时间戳对象返回
ts=calendar.timegm((2018,11,19,16,10,35))
print(ts)

