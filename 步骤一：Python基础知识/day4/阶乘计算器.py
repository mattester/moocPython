#阶乘从1乘以2乘以3乘以4，输出能被5整除的书
#定义初始值
i = 0
sum = 1
while i < 20:
    i = i + 1
    sum = i * sum
    if i % 5 == 0:
        print("{},{}".format(i,sum))
        
