#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import math    
def eular():
    i=item=1
    total = 1
    while item >= 10*(10**(-10)):
        item *= 1/i
        total += item
        i += 1

    return total

def main():
    total=eular()
    print("e=",total)

if __name__=='__main__':
    main()
