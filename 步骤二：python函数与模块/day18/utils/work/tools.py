import os

from day18.utils.work import constants


def get_file_type(file_name):
    """
    根据文件的名称来判断文件的类型
    :param file_name: str 文件名称
    :return: int 文件类型
    -1:位置文件类型
    0：图片类型文件
    1：word文档
    2：excel 文档
    3：ppt 文档
    """
    #默认文件是未知类型的
    result = constants.FILE_TYPE_UNKNOWN
    # result = -1
    # if not os.path.isfile(file_name):
    #     return result
    path_name,ext = os.path.splitext(file_name)
    #将后缀名统一小写
    ext = ext.lower()
    #图片类型的文件
    if ext in ('.png','.jpg','.git','.bmp'):
        result = constants.FILE_TYPE_IMG
    #word文档
    elif ext in ('.doc','.docx'):
        result = constants.FILE_TYPE_DOC
    #excel文档
    elif ext in ('.xls', '.xlsx'):
        result = constants.FILE_TYPE_EXCEL
    #ppt文档
    elif ext in ('.ppt','.pptx'):
        result = constants.FILE_TYPE_PPT
