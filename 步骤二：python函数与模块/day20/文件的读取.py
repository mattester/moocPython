def read_file():
    """读取文件"""
    file_name = 'test2.txt' #保存文件的名字
    #使用绝对路径
    file_path = 'D:\\pythontest\\python基础知识\\步骤二\\day20\\test2.txt'

    #使用普通方式打开文件
    f = open(file_name,encoding="utf-8")
    '''
    读取文件内容（）所有
    rest = f.read()
    关闭
    print(rest)
    读取指定文件内容
    rest = f.read(8)
    print(rest)
    rest = f.read(8)
    print(rest)
    rest = f.read(8)
    print(rest)
    '''
    #随机读取（中文慎用）
    f.seek(5) #跳过5个字符
    print(f.read(5))
    print(f.read(5))
    print(f.read(5))

    #readline（）：读取一行数据，可以指定参数，表示读取前几个字符（字节）
    print(f.readline())
    print(f.readline())
    print(f.readline())


    #readlines（）：读取所有的行，并返回列表
    # rest = f.readlines(4)
    # print(rest)
    # print(len(rest))
    # 读取所有行
    rest = f.readlines(4)
    print(len(rest))
    for i in rest:
        print(i)



    f.close()



if __name__ == "__main__":
    read_file()
