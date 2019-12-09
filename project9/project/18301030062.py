#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
""" project 9 给文件加上行号
"""

import project9_util

text = 'fudan_history.txt'
encoding_used = project9_util.detect_encoding(text)
fo = open('fudan_history.txt' ,'rt',encoding = encoding_used)
newfile = open(project9_util.nl_filename(text),'a+',encoding = encoding_used)
lines = fo.readlines()

i = 0
for line in lines:
    if line.strip() == '':
        newfile.write(line)
        print(line)
    else:
        i += 1
        line = '%-3d'% i + line
        newfile.write(line)
        print(line)
        

fo.close()
newfile.close()
    

    
