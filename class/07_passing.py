"""
    Union注释
"""
from typing import Union
def get_name(name:Union[int,str ])->Union[int,str]:
    return name
if __name__ == '__main__':
    print(get_name("张三"))
    print(get_name(123))