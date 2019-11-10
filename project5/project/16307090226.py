#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def sum(n):
    i = item = 1
    total = 1
    new_item = 1         
    while True:
        item *= i
        new_item = 1/item
        total += new_item
        i += 1
        if new_item < n:
            print(total)
            break
    return

        
if __name__ == '__main__':
    sum(10**(-10))
