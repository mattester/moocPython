"""
编程练习
使用filter函数，求0-50以内（包括50）的偶数
"""
#得到0-50的整数

def use_filter(date):
    """
    求50以内的偶数
    :return:
    """
    rest = filter(lambda n:n % 2 == 0 ,date)
    return rest


if __name__ == '__main__':
    date = list(range(51))
    rust = use_filter(date)
    print(list(rust))
