#用户输入低压和高压
hight = int(input("请输入高压"))
low = int(input("请输入低压"))
if (low > 60 and low < 90) and (hight > 90 and hight < 140):
    print("您的血压正常")
else:
    print("您的血压有问题，请去就诊")
