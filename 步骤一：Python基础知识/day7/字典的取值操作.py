dict2 = {'name':'matt','age':18,'sex':'男'}
#第一种取值方式 通过字典名加中括号里面放入key的形式进行取值
#这种方式和列表的取值类似，列表是通过索引的形式进行取值
name = dict2['name']
print(name)
#第二种取值方式 通过get函数来进行取值
print(dict2.get('name'))
#get函数里面可以赋予默认值，当我们查询一个不存在的key时
print(dict2.get('dept')) #这里会返回默认值none，我们可以进行值得修改
print(dict2.get('dept','其他部门'))#这里查询不到dept，就会返回其他部门

#成员运算符，in和not in，主要看数据是否在字典中，在就返回True，不在就返回False
print('name' in dict2)
print('name' not in dict2)

#遍历字典，有取值方式
#第一种常规的for in 遍历,先找出key，通过字典【key】的方式取值
#这种方式会输出字典内所有的值
for k in dict2:
    v = dict2[k]
    print(v)
#通过.tems函数的方式取值
for k,v in dict2.items():
    print(k,v)







