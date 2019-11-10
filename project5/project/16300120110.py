#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
def main ():

    i = item = 1
    total = 1
    item2 = 1
    while (item2>(1.0/10**10)): 
        item *= i
        item2 = 1 / item
        total += item2
        i += 1

    print("欧拉数为", total)

if __name__ == '__main__':
    main ()
