from datetime import datetime
import random


def write_file():
    """写入文件"""
    file_name = 'write_file.txt'
    #以写入的方式打开内容
    f = open(file_name,'w')
    #写入数据
    f.write('hell0')
    f.write('world')

    #记得关闭
    f.close()

#使用writelines 函数向打开的文件对象写入多行内容
def write_mult_line():
    """
    向文件写入多行内容
    :return:
    """
    file_name = 'write_mult_line.txt' #注意文件的后缀名#
    with open(file_name,'w',encoding='utf-8') as f:
        l = ['第一行','\n','第二行','\n','第三行']
        f.writelines(l)

#用户名id+现在时间写入到一个文件里
def write_user_log():
    """保存用户日志"""
    rest = '用户:{0},时间{1}'.format(random.randint(1000,9999),datetime.now())
    print(rest)
    #我们将得到的日志写入到一个文本里面

    #先将文件的名字保存到一个变量里面，方便重用
    file_name = 'write_user_log.txt'
    with open(file_name,'a',encoding='utf-8') as f: #注意文件的读写模式，多次添加需要用附加模式‘a’
        f.write(rest)
        f.write('\n')

#文件的读和写
def read_and_write():
    '''
    先读取文件在写入文件
    :return:
    '''
    file_name = 'read_and_write.txt'
    with open(file_name,'r+',encoding='utf-8') as f:
        #先将文件读取出来
        read_rest = f.read()
        #如果里面有1就将写入bbb
        #如果里面没有1就写入aaa
        if '1' in read_rest:
            f.write('bbb')
        else:
            f.write('aaa')
        f.write('\n')
if __name__ == '__main__':
    # write_file()
    # write_mult_line()
    # write_user_log()
    # for i in range(5):
#     #     write_user_log()
    read_and_write()