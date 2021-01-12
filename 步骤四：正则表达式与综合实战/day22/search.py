import re
content = "hello,world"
p = re.compile(r'world')
#使用search
rest = p.search(content)
print(rest)
#使用match
rest_match = p.match(content)#match是从头开始找，没找到就返回None
print(rest_match)
