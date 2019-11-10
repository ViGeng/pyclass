#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

#计算自然对数的底数 e 的值 


def main():
    i = k = 1
    n=1
    while True:
        k /= n
        i += k
        if k < 10**-20:
            break
        n += 1
    print('自然对数的底数e的值是',i)


main()
