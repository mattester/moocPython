#导入随机数模块
import random
#将生成的双色球封装成函数
def generate_unionlotto(number):
    for j in range(0, int(number)):
        for i in range(0, 6):
            red = random.randint(1, 33)
            print(red, end=" ")
        blue = random.randint(1, 16)
        print(blue)

while True:
    print("1-双色球随机号")
    print("2-号码百事通")
    print("3-明日天气预报")
    print("0-结束程序")

    c = input("请输入功能编号")
    if c == "1":
        n = input("您要生成几注双色球")
        generate_unionlotto(n)
    elif c == "2":
        print(" ")
    elif c == "3":
        print("")
    elif c == "0":
        print("结束程序")
        break
    else:
        print("您输入的功能有误请重新输入")