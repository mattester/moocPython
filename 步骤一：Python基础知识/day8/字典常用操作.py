#为字典设置默认值
emp = {'name' : 'jacky','grade' : 'b'}
emp2 = {'name' : 'lily'}
print(emp)
#使用成员运算符 not in 来判断grade这个key是不是不在这个字典里
if 'grade' not in emp2 :
    emp2 ['grade'] = 'c' #新增key
print(emp2)
#使用setdefault函数为字典设置默认值
#如果某个key已存在则忽略，如果不存在则设置
emp2.setdefault('grade','b')
print(emp2)

# 2：获取字典的视图（视图就像是字典的键和值（或项）上的窗口）
#获取keys代表获取所有的键
ks = emp.keys()
print(ks)                #dict_keys(['name', 'grade'])
#values 代表获取所有的值
vs = emp.values()
print(vs)            #dict_values(['jacky', 'b'])
#items 代表获取所有的键值对
its = emp.items()
print(its)             # dict_items([('name', 'jacky'), ('grade', 'b')])

#



