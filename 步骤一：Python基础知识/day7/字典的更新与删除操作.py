dict2 = {'name':'matt','age':18,'sex':'男'}
#对单个kv进行更新
dict2['name'] = 'mattest'
print(dict2)
#对多个kv进行更新
#需要使用update函数
dict2.update(name = 'matt',age = '20')
print(dict2)
#字典新增与更新操作相同，有则更新1，无则新增
dict2['dept'] = "研发部"
print(dict2)
dict2['dept'] = "研发部2"
print(dict2)
#字典的删除操作
dict2.pop('name')
print(dict2)
#删除最后一个key,使用popitem函数
dict2.popitem()
print(dict2)
#clear清空字典
dict2.clear()
print(dict2)
