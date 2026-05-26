from data_define import Resource
from file_define import file_reader,file_JSON_reader
if __name__ == '__main__':
    fr = file_reader()
    frj = file_JSON_reader()
    read = fr.data_read("D:/a_develop/py_imformation/file1.txt")
    read_json1 = frj.data_read("D:/a_develop/py_imformation/fileJSON.txt")

    list1 : list[Resource] = read+read_json1
    resource_dict = {}
    for r in list1:
        if r.date in resource_dict:
            resource_dict[r.date].income += r.income
        else:
            resource_dict[r.date] = r
    for i in resource_dict.values():
        print(i)