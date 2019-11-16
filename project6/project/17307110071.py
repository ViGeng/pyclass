#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

#循环结构版本
def main_1():
    result = []
    for i in range(101):
        for j in range(101-i):
            if 5 * i + 3 * j + (1 / 3) * (100 - i - j) == 100:
                result.append([i, j, 100-i-j])

    num = len(result)
    print('总共有%d个解' % num)
    for i in range(num):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % tuple([i+1] + result[i]))


#列表解析式版本
def main_2():
    result = [[i, j, 100-i-j] 
             for i in range(101)
             for j in range(101-i)
             if 5 * i + 3 * j + (1 / 3) * (100-i-j) == 100
             ]

    num = len(result)
    print('总共有%d个解' % num)
    for i in range(num):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % tuple([i+1] + result[i]))

if __name__ == '__main__':
    main_1()
    main_2()
