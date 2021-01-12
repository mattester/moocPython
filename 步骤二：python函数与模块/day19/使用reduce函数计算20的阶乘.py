from functools import reduce


def use_reduce(data):
    result = reduce(lambda x,y:x*y,data)
    print(result)

if __name__ == '__main__':
    data=list(range(1,21))
    rust = use_reduce(data)
    print(rust)