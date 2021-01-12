import re
content = 'hello world'
p = re.compile(r'hello')
rest = p.search(content)
print(rest)
#使用group
if rest:
    print(rest.group())
    print(rest.groups())
print(dir(rest))

def test_id_card():
    """身份证号码正则匹配"""
    id1 = "11010119900307419X"
    id2 = "110101199003073714"
    # p = re.compile(r'(\d{6})(\d{4})((\d{2})(\d{2}))\d{2}(\d{1})([0-9]|X)')
    p = re.compile(r'(\d{6})(?P<year>\d{4})((?P<month>\d{2})(?P<day>\d{2}))\d{2}(\d{1})([0-9]|X)')
    rest1 = p.search(id1)
    print(rest1.group(1)) #110101
    print(rest1.group(2)) #1990
    #groups
    print(rest1.groups()) #('110101', '1990', '0307', '03', '07', '9', 'X')
    #groupdict 返回一个字典，正则表达式必须要有命名
    print(rest1.groupdict())

if __name__ == "__main__":
    test_id_card()