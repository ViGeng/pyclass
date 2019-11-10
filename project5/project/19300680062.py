#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#Project5 作者：19级经济学院 应眺
if __name__ == '__main__':
    e = 1
    i = 1
    t = 1
    while t > 10**-10:
        t = t / i
        e += t
        i = i + 1
    print('e =',e)
