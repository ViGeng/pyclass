#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import project9_util as util


def add_lines():

    encoding_type = util.detect_encoding('fudan_history.txt')
    f = open('fudan_history.txt', encoding = encoding_type)

    new_name = util.nl_filename('fudan_history.txt')      #新文件名
    new_file = open(new_name, mode = 'a', encoding = encoding_type)  #创建新文档

    lines = f.readlines()
    print('for fudan_history.txt -->')

    line_num = 1
    for i in lines:
        if i == '/n' or i.isspace() == True:
            new_file.write(i)                     #写入新文件
            print(i)
        else:
            i = str(line_num) + ' ' + i
            new_file.write(i)
            print(i)
            line_num = line_num + 1

    #print(new_file)                              #如果要打印整个文档直接用read-print流程

    f.close()
    new_file.close()

    pass


def add_lines_2():

    encoding_type = util.detect_encoding('project9_util.py')
    f = open('project9_util.py', encoding = encoding_type)

    new_name_2 = util.nl_filename('project9_util.py')      #新文件名
    new_file_2 = open(new_name_2, mode = 'a', encoding = encoding_type)  #创建新文档

    lines = f.readlines()
    print('for project9_util.py -->')

    line_num = 1
    for i in lines:
        if i == '/n' or i.isspace() == True:
            new_file_2.write(i)                     #写入新文件
            print(i)
        else:
            i = str(line_num) + ' ' + i
            new_file_2.write(i)
            print(i)
            line_num = line_num + 1

    f.close()
    new_file_2.close()

    pass


if __name__ == '__main__':
    add_lines()

    print('-' * 50)

    add_lines_2()

