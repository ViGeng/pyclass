#!/usr/bin/env python

# -*- coding: utf-8 -*-

# File     : 17307130222_pj5.py

# Author   : Zhukaixiang 17307130222

# Date     : 2019/11/2


n = 1

total = 1

item = 1

while item <= 10**10 :
    
    i = n
    item =  1
    
    while i > 0 :
        
        item *= i
        i -= 1

    total += 1/item
    n += 1

print('e=%.50f'%total)
