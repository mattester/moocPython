#新增一个元素
#append（）函数 在列表末端追加新元素
list = ["张三","李四","王五","赵六","钱七","孙八"]
list.append("杨九")
print(list)
#.insert() 在指定索引插入新元素
list.insert(2,"a")
print(list)
#更新索引位置数据，就是替换掉了
list[0] = "b"
print(list)
#更新指定范围的数据
list[3:6] = ["yy","dd","cc"]
print(list)
#删除指定元素
#.remove(元素)
list.remove("李四")
print(list)
#按照索引删除指定元素
# pop(索引)
list.pop(6)
print(list)
#删除多个元素，使用空列表就行
list[0:5] = []
print(list)
