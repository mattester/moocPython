#导入re模块
import re
#原始字符串
content = "one1two2There3four4five5six698"
#将我们的正则表达式编译返回到p对象
p = re.compile('[a-z]+\d+',re.I)#\d代表所有的十进制整数，+代表0或者多个
rest = p.findall(content) #p对象调用findall函数进行匹配
print(rest) #['1', '2', '3', '4', '5', '698'] ,结果会是以一个列表进行输出

#不编译
all_rest = re.findall('[a-z]+\d+',content,re.I)
print(all_rest)