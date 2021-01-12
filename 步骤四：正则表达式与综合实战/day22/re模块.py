import re
#将正则表达式编译，保存一个对象
pattern = re.compile(r"hello") #<re.Match object; span=(0, 5), match='hello'>
#通过match进行匹配
rest = pattern.match("hello,world")
print(rest)
#通过dir查看pattern对象有什么属性和方法
dir(pattern) #这样是看不到的，要进行打印
print(dir(pattern)) #双横杠开头是魔法方法，我们看他的属性就好
print(dir(rest))
