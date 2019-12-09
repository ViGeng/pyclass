#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import project9_util
import string

f1 = open(project9_util.nl_filename('fudan_history.txt'),'w+',encoding=project9_util.detect_encoding('fudan_history.txt'))
f0 = open('fudan_history.txt')

lines = f0.readlines()
i = 0
for item in lines:
    if not item.isspace():
        i += 1
        item = '{0:5d}\t{1}'.format(i,item)
    f1.write(item)
f1.close()
