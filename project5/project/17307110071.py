#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = 1
    i = 0
    e = 0
    while (1 / n) > 1e-10:
        e += 1 / n
        n *= i + 1
        i += 1
    print(e)
