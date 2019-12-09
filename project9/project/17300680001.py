#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project9_util as util

def main():
    text = 'fudan_history.txt'
    encoding = util.detect_encoding(text)
    file = open(text,'r',encoding = encoding)
    lines = file.readlines()
    i = 1
    n = 0

    file1 = util.nl_filename(text)
    new_file = open(file1,'x',encoding = encoding)
    
    for line in lines:
        if len(line.strip()) != 0:
            lines[n] = '%3d  %s'%(i,line)
            i += 1
        n += 1

    new_file.writelines(lines)

if __name__ == '__main__':
    main()




