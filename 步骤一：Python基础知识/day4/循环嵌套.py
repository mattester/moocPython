#打印四个*一排，一共7排
#一个循环里面出4个*，然后把循环运行7次
a = 0
while a < 7:
    i = 0
    while i < 4:
        print("*", end="")
        i = i + 1
    a = a + 1
    print("")