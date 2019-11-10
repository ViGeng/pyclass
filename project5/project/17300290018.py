#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
计算自然对数的底数 e 的值
在求和过程中不允许调用 math 的阶乘函数，也不允许自己实现一个函数来单独计算阶乘
"""

def calculate_e():
    cnt, e_value, res, INF = 1, 0, 1, 1e20
    while cnt <= INF:
        e_value += 1 / cnt
        cnt *= res
        res += 1
    print(e_value)

if __name__ == '__main__':
    calculate_e()
