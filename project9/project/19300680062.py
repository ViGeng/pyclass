#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#project9 作者：19级经济学院 应眺

import project9_util as util

def project9():
    filename = input('请输入文件名')
    encoding = util.detect_encoding(filename)
    with open(filename, encoding = encoding) as file:
        lines = file.readlines()
        
    text = ''
    count = 1
    for line in lines:
        if line.strip():
            text += str(count) + ' ' + line
            count += 1
        else:
            text += line
            
    print(text)
    with open(util.nl_filename(filename), \
              'w', encoding = encoding) as file_nl:
        file_nl.write(text)

if __name__ == '__main__':
    project9()
