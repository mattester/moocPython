#序列类型的互相转换
l1 = ['a','b','c']
t1 = ('d','e','f')
s1 = 'abc123'
s2 = 'abc,123'
r1 = range(1,4)

#转换为列表
l2 = list(l1)
print(l2)
print(t1)
print(list(s1))
print(s2.split(","))
print(list(r1))

#Tuple  转换为元组
print(tuple(s1))
print(tuple(l1))
print(tuple(s2.split(",")))
print(tuple(r1))

#str函数用于将单个数据转为字符串
#join对列表进行连接
print(str(l1))
print(''.join(l1))
print("|".join(t1))
# print(",".join(r1))

s3 = ''
for i in r1:
    print(type(i))
    s3 += str(i)   #i 是int类型，只有为str类型时才能用加法将字符串连接起来
print(s3)