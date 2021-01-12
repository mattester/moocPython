#计算bmi指数
#bmi指数计算公式：体重 / 身高的平方
#获取用户的体重
tizhong = int(input("请输入您的体重"))
hight = float(input("请输入您的身高"))
bmi = tizhong / ( hight * hight)
print(bmi)
if bmi <= 18.4:
    print("您的体重偏瘦")
elif bmi > 18.5 and bmi < 23.9:
    print("您的体重正常")
elif bmi > 24.0 and bmi < 27.9:
    print("您的体重过重")
else :
    print("您的体重肥胖")