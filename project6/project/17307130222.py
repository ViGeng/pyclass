#!/usr/bin/env python

# -*- coding: utf-8 -*-

# File     : 17307130222_pj6_2.py

# Author   : Zhukaixiang 17307130222

# Date     : 2019/11/12



Sol=[[x,y,z] for x in range(0,20) for y in range(0,33) \
for z in (100 - x - y,101 - x - y) if (z%3 == 0) and (5*x + 3*y + z/3 == 100)]

print('总共有%d个解' %len(Sol))

for i in range(len(Sol)):
    print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' %(i+1,Sol[i][0],Sol[i][1],Sol[i][2]))
