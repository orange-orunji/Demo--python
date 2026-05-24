
def str_reverse(s):
    """
    字符串反转
    :param s:待反转的字符串
    :return:反转后的字符串
    """
    return s[::-1]
def substr(s,x,y):
    """
    字符串截取
    :param s:待截取的字符串
    :param x:截取的起始位置
    :param y:截取的结束位置
    :return:截取后的字符串
    """
    return s[x:y]
if __name__ == '__main__':
    print(str_reverse("hello"))
    print(substr("hello",1,3))