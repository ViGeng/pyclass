#!/usr/bin/env python3
# -*- coding:utf-8 -*-

if __name__=='__main__':

    i = item = 1
    total = 1
    while item > 10**(-10):
        item /= i
        total += item
        i += 1
        
    print('e =',total)
