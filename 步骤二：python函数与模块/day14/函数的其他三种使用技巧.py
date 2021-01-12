# 1：序列传参 调用一个*
def calc(a,b,c):
    return (a+b)*c
l = [1,2,3]
print(calc(*l))

# 2:字典传参 使用字典自动为参数赋值 调用二个*
def health_check(name,age,height,weight,hr,hbp,lbp):
    print("您的健康良好")
    print(name)
    print(age)
    print(weight)
param = {"name":"张三","age":"男","height":34,"weight":44,"hr":55,"hbp":33,"lbp":56.8,}
health_check(**param)

# 3：返回值包含多个数据
def get_detail_info():
    dict1 = {
        "employee":[
            {"name":"张三","salary":1800},
            {"name":"李四","salary":2000}
        ],
        "device":[
            {"id":'8837120',"title":"笔记本电脑"},
            {"id":"5556666","title":"台式机电脑"}
        ],
        "assset":[{},{}],
        "project":[{},{}]
    }
    return dict1
print(get_detail_info())
