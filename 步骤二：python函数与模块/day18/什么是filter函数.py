def f(n):
    """判断给定的数是不是奇数"""
    return n % 2 != 0
def use_filer(l):
    """
    获取指定
    :param l:
    :return:
    """
    # rest = filter(lambda n:n %2 !=0,l)
    rest = filter(f,l)
    return rest


if __name__ == "__main__":
    l = [1,2,3,4,5,7,8,9,10,11]
    rest = list(use_filer(l))
    print(rest)