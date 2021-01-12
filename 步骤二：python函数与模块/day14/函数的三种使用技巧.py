#函数的三种使用技巧
#1，设置参数默认值 ，只需要在形参后面增加“=具体值”即可

#关键字传参
def health_check(name,age,height,weight,hr,hbp,lbp):
    print("您的健康良好")
#调用函数
health_check("张三","男",height=32,weight=178,hr=85,hbp=5,lbp=70)

#混合形式传参
def health_check1(name,age,*,height,weight,hr,hbp,lbp):
    print("您的健康良好")
health_check1("张三","男",height=32,weight=178,hr=85,hbp=5,lbp=70)