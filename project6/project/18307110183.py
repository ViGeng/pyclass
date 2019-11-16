#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


#定义函数chicken_1,采用循环结构求解
def chicken_1(num=100, money=100):
    answer = []
    for cock in range(0, num+1):
        for hen in range(0, num-cock+1):
            chick = num - cock - hen
            if cock * 5 + hen * 3 + chick / 3 == money:
                answer.append([cock,hen,chick])
    return answer


#定义函数chicken_2,采用列表解析式求解
def chicken_2(num=100, money=100):
    answer = [[cock, hen, num - cock - hen]
              for cock in range(0, num+1)
              for hen in range(0, num-cock+1)
              if cock * 5 + hen * 3 + (num - cock - hen
                                       ) / 3 == money]
    return answer


#调用chicken_1
def main_1():
    print('#循环结构求解')
    answer = chicken_1()
    if not answer:
        print('找不到解')
    else:
        print('总共有%d个解'% len(answer), end='\n')
        for i in range(0, len(answer)):
            print('解%s:' % (i+1),
                  '鸡翁',answer[i][0],
                  '鸡母',answer[i][1],
                  '鸡雏',answer[i][2],
                  sep='\t', end='\n')

#调用chicken_2
def main_2():
    print('#列表解析式求解')
    answer = chicken_2()
    if not answer:
        print('找不到解')
    else:
        print('总共有%d个解'% len(answer), end='\n')
        for i in range(0, len(answer)):
            print('解%s:' % (i+1),
                  '鸡翁',answer[i][0],
                  '鸡母',answer[i][1],
                  '鸡雏',answer[i][2],
                  sep='\t', end='\n')


if __name__ == '__main__':
    main_1()
    print()
    main_2()
