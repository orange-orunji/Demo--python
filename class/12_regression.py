"""
    递归学习.递归访问文件夹案例
"""
import os

def print_file_dits(path):
    dirs = []
    if os.path.exists(path):
        for i in os.listdir(path):
            newPath = path+'/'+i
            if os.path.isdir(i):
                dirs += print_file_dits(newPath)
            else:
                dirs.append(newPath)

    return dirs
if __name__ == '__main__':
    dits = print_file_dits("D:/a_develop")
    for dit in dits:
        print(dit)
