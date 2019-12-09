#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
""" project 9 给文件加上行号
"""


def detect_encoding(text):
    """探测文件的编码方式
    参数：文件名， 返回探测到的编码方式
    """
    
    # UTF-8-SIG
    encodings = 'ASCII', 'UTF-8', 'GBK'

    for encoding in encodings:
        try:
            with open(text, encoding=encoding) as f:
                f.read(100)
            break
        except UnicodeDecodeError:
            pass
    return encoding

def nl_filename(name):
    """ 返回一个新的文件名，传递的参数name为文件名
    """

    if name.endswith(('.txt', '.py')):
        dot_pos = name.rindex('.')
        return name[0:dot_pos] + '_nl' + name[dot_pos:]
    else:
        return name + '_nl'

if __name__ == '__main__':
     filename = input('请输入需要添加行号的文本文件名称:')
     filename_nl = nl_filename(filename)
     code_format = detect_encoding(filename)
     key = False
     line_count = 0
     newline = ''

     data = []
     blank_characters = [' ','\n','\t']
     with open(filename, 'r+', encoding = code_format) as oldfile:
          data = oldfile.readlines()
          with open(filename_nl, 'a+', encoding = code_format) as newfile:
               for line in data:
                    key = 0
                    for i in line:
                         if i not in blank_characters:
                              key = True
                    if key:
                         line_count += 1
                         newline = str(line_count) + ' ' + line
                    else:
                         newline = line
                    newfile.write(newline)

print('已在文件夹中生成fudan_history_nl.txt')











                              
