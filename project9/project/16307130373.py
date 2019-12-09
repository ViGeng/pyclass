#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import project9_util
import string 
import re

def get_new_file(text):
    new_file_name = project9_util.nl_filename(text)
    encoding = project9_util.detect_encoding(text)
    list_text = open(text,mode='r',encoding=encoding).readlines()
    new = []
    num = 0#记录行号
    #print(list_text)
    pattern =re.compile(r'\s+')#匹配出多个空格类字符组成的字符串，eg.('    \n')
    for i in range(len(list_text)):
        r = re.match(pattern,list_text[i])
        if r == None:
            num += 1
            item = list(list_text[i])
            item[0:0] = (str(num)+'   ')
            item = ''.join([str(k) for k in item])
        else:
            item = '\n'
        new.append(item)
        if new[0] == '\n':
            new = new[1:]
    with open(new_file_name,mode='w',encoding=encoding) as f:
        for k in new:
            f.write(k+'\n')
    return new_file_name

if __name__ =='__main__':
    get_new_file('fudan_history.txt')




        

