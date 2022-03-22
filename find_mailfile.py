# -*- coding: utf-8 -*-
# @Date    : 2021-06-02 21:54:08
# @Author  : fh
# @File    : find_mailfile.py
'''查找某目录中的最新文件'''

import os


class FindNewFile:

    def find_NewFile(self, path):
        #获取文件夹中的所有文件
        lists = os.listdir(path)
        #对获取的文件根据修改时间进行排序
        lists.sort(key=lambda x: os.path.getmtime(path + '\\' + x))
        #把目录和文件名合成一个路径
        file_new = os.path.join(path, lists[-1])
        return file_new


if __name__ == '__main__':
    newfile = FindNewFile().find_NewFile('test_Report')
    print(newfile)