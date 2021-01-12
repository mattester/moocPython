#定义一个员工记事本
jishiben = []
#把员工信息保存起来
while True:
    list = input("输入员工信息")
    #将输入的信息分割成列表
    list_info = list.split(",")
    if list == "": #程序结束一定要在最前面，不然，下面的不等于3会直接忽略到这条语句重新循环
        print("程序结束拜拜")
        break
    if len(list_info) != 3:
        continue
    jishiben.append(list_info)
    for p in jishiben:
        print("{},{},{}".format(p[0],p[1],p[2]))
