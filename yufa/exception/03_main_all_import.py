"""
    模块导入的main和all使用
"""
#
# from my_model import *
# test1(1,2)
# test2(1,2)
from my_utils import str_util
# file_util.print_file_info("D:/a_develop/py_imformation/bill.txt")
# file_util.append_to_file("D:/a_develop/py_imformation/bill.txt.bak","黑马程序员")
print(str_util.str_reverse("黑马程序员"))
print(str_util.substr("黑马程序员", 0, 3))