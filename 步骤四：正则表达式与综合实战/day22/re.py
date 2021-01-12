import re
#将正则表达式编译，保存一个对象
pattern = re.compile(r"hello") #<re.Match object; span=(0, 5), match='hello'>
#通过match进行匹配
rest = pattern.match("hello,world")
print(rest)
#通过dir查看pattern对象有什么属性和方法
dir(pattern)
