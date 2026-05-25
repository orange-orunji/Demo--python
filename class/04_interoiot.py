"""
    封转 的练习
"""
class phone:
    __is_5g_enable = None
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
if __name__ == '__main__':
    phone = phone()
    phone.call_by_5g()