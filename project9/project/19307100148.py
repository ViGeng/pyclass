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

def write_file(file='fudan_history.txt'):
    f1 = open(file,'r',encoding = 'GBK')
    f3 = open('text_txt','w',encoding = 'GBK')
    for line in f1.readlines():
        if line == '\n':
            line = line.strip("\n")
        f3.write(line)
    f1.close()
    f3.close()
    with open('text_txt',encoding = 'GBK') as f:
        Sentences = f.readlines()
        for i in range(1,len(Sentences)):
            Sentences[i]=str(i)+' '+Sentences[i]
    f.close()
    with open('fudan_history2.txt','w+') as f2:
        f2.writelines(Sentences)
    f2.close()

def nl_filename(name):
    """ 返回一个新的文件名，传递的参数name为文件名
    """

    if name.endswith(('.txt', '.py')):
        dot_pos = name.rindex('.')
        return name[0:dot_pos] + '_nl' + name[dot_pos:]
    else:
        return name + '_nl'


if __name__ == '__main__':
    print('%s-->%s: %s' % (__file__, nl_filename(__file__), detect_encoding(__file__)))

    text = 'fudan_history.txt'
    print('%s-->%s: %s' % (text, nl_filename(text), detect_encoding(text)))

    write_file()
    
