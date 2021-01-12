# #遍历列表
list = ["张三","李四","王五","赵六","钱七","孙八","赵六"]
# #for循环用于遍历列表
# #for 迭代变量 in 可迭代对象
# i = 0
# for p in list:
#     if p == "赵六":
#         print(p,i) #正序索引
#     i += 1
#
# # 倒序索引
# count = len(list)
# print(count)
# i1 = 0
# for p in list:
#     if p == "赵六":
#         rl = count * -1 + i1
#         print(p ,rl)
#     i1 += 1

#使用while循环
i2 = 0
count = len(list)
while i2 < count:
    r2 = list[i2]
    print(r2,i2)
    i2 += 1