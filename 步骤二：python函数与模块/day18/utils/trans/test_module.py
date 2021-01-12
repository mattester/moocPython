from datetime import datetime

from day18.utils.trans.tools import gen_trans_id
from day18.utils.trans import tools as trans_tools
from day18.utils.work import tools as work_tools

def test_trans_tool():
    """测试trans包下的tools模块"""
    id1 = trans_tools.gen_trans_id()
    print(id1)
    date = datetime(2015,12,2,16,45,20)
    id2 = trans_tools.gen_trans_id(date)
    print(id2)

def test_work_tool():
    """测试work模块"""
    file_name = "D:\\python学习文件夹\\test.jpg"
    rest = work_tools.get_file_type(file_name)
    print(rest)

if __name__ == '__main__':
    test_trans_tool()
    test_work_tool()




