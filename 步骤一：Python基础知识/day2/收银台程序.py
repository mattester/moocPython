#商品的单价，名称，数量,输入
# 普通字符 9折
# 阿里字符 再打9折
#输入商品名称，单价
name = input("商品名称")
danjia = input("商品单价")
sum = input("商品数量")
zhongjia = float(danjia) * int(sum)
zhifu = zhongjia * 0.9
alzhifu = zhifu * 0.9
print("您购买的商品为"+name)
print("您购买的商品总价为"+"str（zhifu）")
print("使用阿里支付金额为"+"alzhifu")
