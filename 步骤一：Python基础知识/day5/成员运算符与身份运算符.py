#成员运算符，在指定的序列中找到值返回trun，否则返回false
#定义一个数组
a = ["abc","def","ghj"]
if "abcd" in a:
    print("我在里面")
else:
    print("我不在里面")

#身份运算符，判断两个变量是不是引用自一个变量
b = 55
c = 55.0
g = 33
if b is c:
    print("我两一样的哦")
else:
    print("我两不一样")