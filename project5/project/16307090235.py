#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

"""在求和过程中不允许调用 math 的阶乘函数，
   也不允许自己实现一个函数来单独计算阶乘
提示：
1. 注意观察比较相邻项之间的关系，
2. 求和到什么时候结束？某项小于某个极小的值，比如 10 的-10 次方
"""


def sum_factorial(n):
    item = i = 1
    total = 1
    item_last = 1
    while True:
        item *= i
        item_last = 1/item
        total += item_last
        i += 1
        if item_last < n:
            print(total)
            break
    return

if __name__ == '__main__':
    total = sum_factorial(10**-10) 



    
