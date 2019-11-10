#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def main():
    i = 1
    item = 1
    total = 1
    while True:
        total += item ** (-1)
        i += 1
        item *= i
        if item ** (-1) < 10 ** (-10):
            break
    print('e = %.10f' % total)
    return None

if __name__ == '__main__':
    main()
