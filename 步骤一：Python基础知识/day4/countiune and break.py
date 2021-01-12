#break 种植循环
i = 0
while i < 3 :
    phone = input("请输入手机号")
    i = 1 + i
    if phone == "1234567890123" :
        print("您输入的手机号正确")
        break
print("欢迎拨打10086")