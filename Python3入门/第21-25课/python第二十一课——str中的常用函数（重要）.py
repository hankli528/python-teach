#！/usr/bin/env python
# Author:Hank

'''
演示str中常用的一些函数：
'''

'''
1.join()：将容器对象以某种特定的格式(字符串)进行拼接组合，最后以字符串的形式返回
'''
lt=['i','love','you','very','much']

str1='-'.join(lt)
# print(str1,type(str1))
# print(str.join('*',lt))
# print(' '.join(lt))

#报错：需要显示的在第一个参数位置定义链接的格式(串)
# print(str.join(lt))


'''
2.rjust()：将字符串数据以规定的长度进行存储，内容在右侧显示，如果长度不足，左侧补规定的字符

ljust()：将字符串数据以规定的长度进行存储，内容在左侧显示，如果长度不足，右侧补规定的字符

center()：将字符串数据以规定的长度进行存储，内容在中间显示，如果长度不足，左右两侧补平分规定的字符

zfill()：将字符串数据以规定的长度进行存储，内容在右侧显示，如果长度不足，左侧补0字符
'''
str1='i love you very much'
# print(str1.ljust(50,'*'))
# print(str1.ljust(50,'-'))
# print(str.rjust(str1,30,'$'))
# print(str1.center(60,'0'))
# print(str1.zfill(40))


'''
3.rstrip()：剔除右侧匹配的字符内容，最终返回一个新的字符串数据；注意：原串不会发生变化

lstrip()：剔除左侧匹配的字符内容，最终返回一个新的字符串数据；注意：原串不会发生变化

strip()：剔除左、右两侧匹配的字符内容，最终返回一个新的字符串数据；注意：原串不会发生变化
'''
str2='\\ ,,, i hate you very much  \,, '
# print(str2.lstrip('\ ,'))
# print(str2.rstrip(',\ '))
# print(str2.strip(' \, '))


'''
4.split()：如果不传递参数，那么默认按照空格、换行都匹配进行切割，将切完的子串以列表的形式返回，如果传递参数，那么就是以参数的格式(字符串)进行切割，返回的仍然是切完子串的列表对象

splitlines()：不用传递参数，默认就是以换行符(' ')进行切割，将切完的子串以列表的形式返回
'''
str3='i love\n you very\n much'
# print(str3.split(' '))
# print(str3.split())
# print(str3.split('\n'))
# print(str3.splitlines())


'''
5.index()：返回匹配的字符串的索引内容，如果不匹配，报错
'''
str4='abcdefg123'
# print(str4.index('b'))
# print(str4.index('bcd'))

'''
如果字符内容不在元串中，那么会报错：ValueError
如果字符内容在原串中多次出现，那么返回第一次匹配成功的下标位置
'''
# print(str4.index('bcde'))
# print(str4.index('aa'))


'''
6.count()：返回串在原串中出现的次数，如果一次都没有出现，返回0
'''
str5='aabcdeaageaa123'
# print(str5.count('a'))
# print(str5.count('aa'))
# print(str5.count('xy'))


'''
7.replace()：将原串中的某内容以新串进行替换，默认全部替换；也可以显示的定义替换的次数
'''
str6='北京啊北京，我为你骄傲！北京啊北京，我为你自豪'
str7=str6.replace('北京','hank')
str8=str6.replace('北京','hank',2)
# print(str6)
# print(str7)
# print(str8)


'''
8.find()：返回字符串在原串中首次出现的位置

rfind()：返回字符串在原串中最后一次出现的位置
'''
str9='山不在在高，有仙则名；水不在在深，有龙则灵；斯是在在陋室，惟吾德馨。'
# print(str9.find('在在'))
# print(str9.rfind('在在'))

'''
如果字符串内容在原串中不存在，返回-1；特殊情况特殊记忆
'''
# print(str9.rfind('在在在'))


'''
9.startswith()：判断某字符串是否是原串的开始部分，返回布尔值

endswith()：判断某字符串是否是原串的结束部分，返回布尔值
'''
str10='haha abcdef ghijk 12345 hehe'
# print(str10.startswith('h'))
# print(str10.startswith('ha'))
# print(str10.startswith('haha'))
# print(str10.startswith('aha'))
# print(str10.endswith('he'))
# print(str10.endswith('ehe'))
# print(str10.endswith('hhe'))


'''
10.lower()：将字符串中英文字符转换为全小写

upper()：将字符串中英文字符转换为全大写

capitalize()：将字符串中英文字符首字母大写，其余字母小写

title()：将字符串中英文字符的部分分块，每块的首字母大写，其余字母小写

swapcase()：将字符串中原本英文字符大写的转为小写，小写转为大写
'''
str11='today is tuseday PM'
# print(str11.lower())
# print(str11.upper())
# print(str11.capitalize())
# print(str11.title())
# print(str11.swapcase())


'''
11.isalnum()：判断字符串中是否只有英文字符或者数字字符

isalpha()：判断字符串中是否只有英文字符

isdecimal()：判断字符串中是否只有数字字符

isdigit()：判断字符串中是否只有数字字符

islower()：判断字符串中英文字符是否全部都是小写

isupper()：判断字符串中英文字符是否全部都是大写

istitle()：判断字符串中各个英文部分的首字母是否全部都是大写
'''

str12='A123Yxnda$&'
print(str12.isalnum())
print(str12.isalpha())
print(str12.isdecimal())
print(str12.isdigit())
print(str12.islower())
print(str12.isupper())
print(str12.istitle())