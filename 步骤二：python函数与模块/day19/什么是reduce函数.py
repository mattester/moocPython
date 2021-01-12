#求列表的和
from functools import reduce


def get_sum(l):
    """
    根据给定列表的项，求所有的项的和
    :param l: 列表，int
    :return: 返回列表的和
    """
    rest = 0
    for i in l:
        rest = rest + i
    return rest

def get_sum_use_py(l):
    """
    使用python内置的sum（）进行求和
    :param l:
    :return:
    """
    return sum(l)

def f(m,n):
    return m+n

def get_sum_use_reduce(l):
    """
    s使用reduce进行求和
    :param l:
    :return:
    """
    return reduce(f,l)

def get_sum_use_lambda(l):
    """
    s使用lanbda进行求和
    :param l:
    :return:
    """
    return reduce(lambda m,n:m+n,l)

if __name__ == "__main__":
    l = [1,2,3,4,5,6,7,8,9]
    rust = get_sum(l)
    print(rust)
    rust = get_sum_use_py(l)
    print(rust)
    print("_______________________")
    rust = get_sum_use_reduce(l)
    print(rust)
    print("_______________________")
    rust = get_sum_use_lambda(l)
    print(rust)
