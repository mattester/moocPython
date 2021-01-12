#将列表的内容反转输出
# 使用for_in 遍历
list = ["张三","李四","王五","赵六","钱七","孙八","赵六"]
#列表长度
daoxu = -1
i = 0
count = len(list)
while i <count:
    persons = list[daoxu]
    print(persons)
    i += 1
    daoxu -= 1

#使用.reverce()方法用于反转列表
list.reverse()
print(list)

#使用sort（）降序排序函数
number = [44,34,67,23,567,33]
number.sort(reverse=True)
print(number)

