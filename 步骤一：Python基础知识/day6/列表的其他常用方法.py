list = ["张三","李四","王五","赵六","钱七","孙八"]
#统计一个元素出现的次数
#count函数
chishu = list.count("钱七")
print(chishu)
#追加操作，在列表后面进行增加元素
list.append("爸爸")
print(list)
list.extend(["妈妈","爷爷"])
print(list)
#in 成员运算符，判断一个元素时候在列表里面，如果有返回True，否则返回False
list.remove("爸爸")
if "爸爸" in list:
    print("在里面")
else:
    print("不在里面")

if "爸爸" not in list:
    print("不在里面")
else:
    print("在里面")

#复制一个列表 copy()
list3 = list.copy()
print(list3)
print(list is list3)
list4 = list3
print(list3 is list4)

#清空一个列表 clear()
list.clear()
print(list)

