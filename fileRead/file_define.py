"""
    定义文件读取的类型
"""
import json

from fileRead.data_define import Resource
class FileReader:
    def data_read(self,patch) -> list:
        pass

class file_reader(FileReader):
    def data_read(self,patch):
        result : list[Resource] = []
        fr = open(patch, "r", encoding="UTF-8")
        for i in fr.readlines():
            split = i.strip().split(",")
            result.append(Resource(split[0],split[1],int(split[2]),split[3]))
        fr.close()
        return result

class file_JSON_reader(FileReader):
    def data_read(self,patch):
        result : list[Resource] = []
        fr = open(patch, "r", encoding="UTF-8")
        for line in fr.readlines():
            load_split = json.loads(line)
            result.append(Resource(load_split["date"],load_split["order_id"],int(load_split["money"]),load_split["province"]))
        fr.close()
        return result
if __name__ == '__main__':
    fr = file_reader()
    read = fr.data_read("D:/a_develop/py_imformation/file1.txt")
    for i in read:
        print(i)
    frjSON = file_JSON_reader()
    read = frjSON.data_read("D:/a_develop/py_imformation/fileJSON.txt")
    for i in read:
        print(i)