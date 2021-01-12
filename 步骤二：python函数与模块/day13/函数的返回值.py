##参数是函数的输入数据，而返回值这是函数的输出结果
#汇率计算器
def calc_exchange_rate(amt,source,target):
    if source == "CNY" and target == "USD":
        resulf = amt / 7516
        return resulf
r = calc_exchange_rate(100,"CNY","USD")
print("转换结果为：{}".format(r,"#0.000"))



