#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
""" project 9 给文件加上行号
"""

import project9_util as util

def read_file():
    """读取文件"""
    
    encoding = util.detect_encoding('fudan_history.txt')
    f = open('fudan_history.txt', 'r', encoding=encoding)
    return f, encoding

def count_lines(file):
    """统计有效行数"""
    
    max_line = 0
    for line in file:
        if not line.isspace():
            max_line += 1
    return max_line

def add_number(file, max_line, encoding):
    """添加行号并写入到新文件"""

    output_file_name = util.nl_filename('fudan_history.txt')
    output_file = open(output_file_name, 'wt', encoding=encoding)

    number = 0
    space = len(str(max_line))
    for line in file:
        if line.isspace():
            new_line = line
        else:
            number += 1
            new_line = str(number) + ' ' * (space - len(str(number)) + 1) + line
        output_file.write(new_line)
    output_file.close()
        

def main():
    f, encoding = read_file()
    max_line = count_lines(f)
    f.seek(0)
    add_number(f, max_line, encoding)
    f.close()

if __name__ == '__main__':
    main()
