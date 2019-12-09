#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import project9_util
import string
file = open(project9_util.nl_filename('fudan_history.txt'),'w+',encoding=project9_util.detect_encoding('fudan_history.txt'))
f = open('fudan_history.txt')
s = f.readlines()
k = 0
for i in s:
    if not i.isspace():
        k=k+1
        i='{0:5d}\t{1}'.format(k,i)
    file.write(i)
file.close()
