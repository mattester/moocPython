#集合的遍历
college1 = {"哲学","经济学","法学","教育学"}
for c in college1:
    print(c)

#判断元素存在
print("哲学" in college1)
print("计算机学" in college1)

#集合不支持按索引提取元素
#print(college1[3])

#新增数据一次只能添加一个元素，add方法
college1.add("文学")
print(college1)

#update方法一次添加多个元素
college1.update(["计算机学","人工智能学"])
print(college1)

#remore方法删除一个元素
college1.remove("生物学")
print(college1)
#更新操作要删除原有元素，然后进行添加元素
#remore删除不存在的元素会报错

#discard方法，如果遇到不存在的元素则会忽略删除操作
#discard() 方法用于移除指定的集合元素。
#该方法不同于 remove() 方法，因为 remove() 方法在移除一个不存在的元素时会发生错误，而 discard() 方法不会

#集合不支持提取和更新，如果需要更新，则需要删除原有元素，然后进行添加