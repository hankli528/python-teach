#！/usr/bin/env python
# Author:Hank

'''
案例五：求两个列表元素的和,返回新列表
lt1 = [1,2,3,4]
lt2 = [5,6]
效果：[6,8,10,12]
'''
lt1=[1,2,3,4]
lt2=[5,6]
# print(list(map(lambda x,y:x+y,lt1,lt2)))


'''
案例六：求字符串中每个单词的长度
效果：[7,2,8]
content = 'Welcome To ShangHai'
'''
#切割是关键，因为一切就是列表了，按照什么切呢？直接split()切
content='Welcome To ShangHai'
word_list=content.split()
mo=map(len,word_list)
print(list(mo),type(mo))