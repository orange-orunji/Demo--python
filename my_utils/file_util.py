
def print_file_info(file_name):
    """
    打印文件信息
    :param file_name: 文件名
    :return:  无
    """
    fr = open(file_name, "r", encoding="UTF-8")
    try:
        for i in fr:
            print(i)
    except Exception as e :
        print(e)
    finally:
        fr.close()
def append_to_file(file_name,data):
    """
    追加数据
    :param file_name: 写入目标文件名
    :param data:  追加的数据
    :return: 无
    """
    fa = open(file_name, "a", encoding="UTF-8")
    fa.write(f"\n{data}")
    fa.close()
if __name__ == '__main__':
    print("开始执行...")
    print_file_info("D:\\a_develop\\py_imformation\\bill.txt")
    append_to_file("D:\\a_develop\\py_imformation\\bill.txt.bak","追加的数据")