#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-


def main():
    total = 1
    i = item = 1
    
    while True:
        total += 1 / item
        i += 1
        item *= i
        if 1 / item < 10 ** (-10):
            break
    print('e = %f' % total)


if __name__ == '__main__':
    main()
