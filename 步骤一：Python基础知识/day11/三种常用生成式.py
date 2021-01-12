#三种常用生成式
#三种内置生成式
# 1:列表生成式
# 2：字典生成式
# 3：集合生成式

#生成式语法 【被追加的元素 循环语句或者判断语句】

#列表生成式
list1 = []
list1 = [i*10 for i in range(10,20)]
print(list1)
#展开
list1 = []
for i in range(10,20):
    list1.append(i*10)
print(list1)

#列表生成接if语句
lst3 = [i *10 for i in range(10,20) if i % 2 ==0]
print(lst3)
#展开
lst3 = []
for i in range(10,20):
    if i % 2 == 0:
        lst3.append(i*10)
print(lst3)

#两个循环
lst4 = [i * j for i in range(1,5) for j in  range(1,5)]
print(lst4)

#展开
lst4 = []
for i in range(1,5):
    for j in range(1,5):
        lst4.append(i*j)
print(lst4)

#字典生成式
lst5 = ["张三","李四","王五"]
dict1 = {i+1:lst5[i] for i in range(0,len(lst5))}
print(dict1)
#展开
dict2 = {}
for i in range(0,len(lst5)):
    dict2[i+1] = lst5[i]
print(dict2)

#集合生成式
set1 = {i * j for i in range(1,4) for j in range(1,4) if i == j}
print(set1)
#展开
for i in range(1,4):
    for j in range(1,4):
        if i == j:
           set1.add( i * j)
print(set1)



