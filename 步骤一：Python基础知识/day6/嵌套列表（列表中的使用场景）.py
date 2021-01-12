emp_list = []
while True:
    info = input("请输入员工信息:")
    if info == "":
        print("程序结束")
        break
    info_list = info.split(",")
    if len(info_list) != 3:
        print("输入格式不正确，请重新输入")
        continue
    emp_list.append(info_list)
    for emp in emp_list:
        print("{n},年龄:{a},工资：{s}".format(n=emp[0],a=emp[1],s=emp[2]))
