"""
    继承关系案例
"""
class phone:
        __is_5g_enable = None
        P = "ITCAST"
        def __init__(self):
            self.__is_5g_enable = True

        def __check_5g(self):
            if self.__is_5g_enable:
                print("5g已开启")
            else:
                print("5g已关闭,使用4g网络")

        def call_by_5g(self):
            self.__check_5g()
            print("正在通话中")
class NFC:
    __is_NFC_enable = False
    def nfc_read(self):
        print("NFC读卡已开启")
    def nfc_write(self):
        print("NFC写卡已开启")
class read_X:
    __is_read_X_enable = False
    P = "X"
    def read_X(self):
        print("红外线已开启")
class Phones(phone, NFC, read_X):
    P = "hm"
    def __init__(self):
        print(super.P)
"""
    继承关系
    phone -> NFC -> Phones
    phone -> read_X -> Phones
"""

if __name__ == '__main__':
    phones = Phones()
    phones.call_by_5g()
    phones.nfc_read()
    phones.nfc_write()
    phones.read_X()
    print(phones.P)
