#将小明的姓名，年龄，身高，性别，班级格式化输出
name = "小明"
age = 15
hight = 180
sex = "男"
club = "三班"
#常规输出
xiaomin = "这位同学的姓名是"+ name+",年龄是"+ str(age)+",身高"+ str(hight) + ",性别"+sex+",班级"+str(club)
print(xiaomin)
# 字符串格式化
ta = "我叫{},年龄是{},身高{},性别{},班级{}".format(name,age,hight,sex,club)
print(ta)
tata = "我叫{a},年龄是{b},身高{c},性别{d},班级{e}".format(a=name,b=age,c=hight,d=sex,e=club)
print(tata)