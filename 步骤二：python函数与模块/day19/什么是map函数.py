def pow_number(l):
    """
    根据给定的列表数据，计算里面每一项的立方
    :param l: 列表数据
    :return: 原来列表中每一项的立方
    """
    rest_list = []
    for x in l :
        rest_list.append(x*x*x)
    return rest_list

def f(n):
    return n*n*n
def pow_num_use_map(l):
    """
    使用map函数计算给定项列表的每一次立方
    :param l: 列表数据
    :return: 原来列表的每一项的立方
    """
    return map(f,l)

#使用lambda函数
def pow_num_use_map_lambda(l):
    """
    使用map函数计算给定项列表的每一次立方
    :param l: 列表数据
    :return: 原来列表的每一项的立方
    """
    return map(lambda n:n*n*n,l)

if __name__ == '__main__':
    l = [1,2,3,4,5,6]
    rest = pow_number(l)
    print(rest)
    rest = pow_num_use_map(l)
    print(list(rest))
    print("_________________________________")
    rest = pow_num_use_map_lambda(l)
    print(list(rest))
