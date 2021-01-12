import re
s = 'one1two2there3four4five5six666'
p = re.compile(r'\d+')
rest = p.split(s,2)
print(rest) #['one', 'two', 'there', 'four', 'five', 'six', '']

#sub()函数
p = re.compile(r'\d+')
rest = p.sub('@',s)
print(rest)

#使用replace替换
rest = s.replace("1","@")
print(rest) #one@two2there3four4five5six666

#使用正则表达式更换位置
s2 = "hello world"
p2 = re.compile(r'(\w+) (\w+)') #第一个括号代表hello，第二个括号代表world
rest_pos = p2.sub(r'\2 \1',s2) #\2 \1，代表位置的改变，s2改变的字符串位置
print(rest_pos)

#替换并改变内容
def f(m):
    return m.group(2).upper() + ' ' + m.group(1) #upper()函数代表大写
rest_change = p2.sub(f,s2) #sub里面可以是函数，也可以是正则表示
print(rest_change) #WORLD hello

#将以上函数进行简写 ,使用lambda匿名函数
rest_lambda = p2.sub(lambda m:m.group(2).upper() + ' ' + m.group(1),s2)
print(rest_lambda) #WORLD hello
