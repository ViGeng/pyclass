#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


if __name__ == '__main__':
    (i,item,e) = (1,1,1)
    while 1 / item >= 10 * 10**(-10):
        item = item * i
        e = e + 1 / item
        i = i + 1
    print('%3s %.20f'%('e =',e))

