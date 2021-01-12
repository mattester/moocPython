def use_map(data):
    """
    求元组内各项的5次方
    :param data:列表数据
    :return:经过函数运算的返回结果
    """
    result = map(lambda n:pow(n,5),data)
    return result

if __name__ == '__main__':
    date = (2,4,6,8,10,12)
    result = use_map(date)
    print(tuple(result))
