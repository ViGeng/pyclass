#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#Project6 作者：19级经济学院 应眺

def solution1():
    answer = []
    for cock in range(101):
        for hen in range(101 - cock):
            chick = 100 - cock - hen
            if 5 * cock + 3 * hen + 1/3 * chick == 100:
                answer.append([cock, hen, chick])
    print('总共有%d个解'%len(answer))
    for i in range(len(answer)):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d'%(i + 1, answer[i][0], answer[i][1],answer[i][2]))

def solution2():
    answer = [[cock, hen, 100 - cock - hen] for cock in range(0,101) 
        for hen in range(101-cock) if 5 * cock + 3 * hen + 1/3 * (100 - cock - hen) == 100]
    print('总共有%d个解'%len(answer))
    for i in range(len(answer)):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d'%(i + 1, answer[i][0], answer[i][1],answer[i][2]))

if __name__ == '__main__':
    solution1()
    solution2()
