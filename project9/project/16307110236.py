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
    print('%s-->%s: %s' % (__file__, nl_filename(__file__), detect_encoding(__file__)))
    text = 'fudan_history.txt'
    print('%s-->%s: %s' % (text, nl_filename(text), detect_encoding(text)))
    _file = './fudan_history.txt'
    _encode=detect_encoding(_file)
    print(_encode)
    #打印编码，便于调试
    f=open(_file,"r",encoding=_encode)
    fmodifyed=open(nl_filename(_file),"w+",encoding=_encode)
    #用指定的编码方式打开需要修改的文件和准备写入的文件

    line=f.readline()
    i=0
    while line:
        #对每一行进行处理
        test_operator = 0
        
        for a in line:
            if a!=" " and a!="\n" :
                test_operator = 1
                
        if  test_operator == 1:
            i=i+1
            print("加行号!"+str(i))
            print(line)
            newline=('%3d  '%i) + line
            fmodifyed.write(newline)
        else :
            fmodifyed.write(line)
            print("空行！")
        line=f.readline()
        #读取新的一行
    
    f.close()
    fmodifyed.close()
    #关闭文件

    
