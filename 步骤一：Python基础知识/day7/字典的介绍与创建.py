# 创建一个字典
dict1 = {} #空的字典
dict2 = {'name':'matt','age':18,'sex':'男'}
print(dict2)
# 通过dict函数创建字典
dict3 = dict(name='汪峰',age='18',sex='男')
print(dict3)
# 利用一个序列创建一个key
dict4 = dict.fromkeys(['name','sex','age','hiredate'],'N/A')
print(dict4)


