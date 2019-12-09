#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
# File     : 17307130222_pj9.py

# Author   : Zhukaixiang 17307130222

# Date     : 2019/12/01

def file_processing(file_name):

    import project9_util as util

    encoding=util.detect_encoding(file_name)
    
    with open(file_name,'r',encoding=encoding) as file:
        lines = file.readlines()

    new_filename=util.nl_filename(file_name)

    f=open(new_filename,'w',encoding=encoding)
    
    i=1
    for line in lines:
        if not(line == '\n') and len(line) and not(line.isspace()):
            f.write('%d %s' %(i,line))
            i+=1
        else:
            f.write(line)
    f.close

if __name__ == '__main__':
    text='fudan_history.txt'
    file_processing(text)
