import pickle
from person import Person

'''
演示对象序列化和反序列化操作：
'''

#创建Person对象
p = Person('貂蝉',23,'女',163.0,92,'惊艳')

'''
将p对象序列化到文件person.txt中
'''
fw=open('person.txt','wb',encoding='utf-8')
pickle.dump(p,fw)
fw.close()


