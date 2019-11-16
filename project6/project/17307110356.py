#! /usr/bin/env python3
# -*- coding: utf-8 -*-


def chicken_100_problem_loop(num=100, money=100):
    '''100只鸡100元，5元/鸡翁male，3元/鸡母female，1元/3鸡雏babies
    '''
    solve = []
    for males in range(0, num+1):
        for females in range(0, num+1):
            if males * 5 + females * 3 + (num - males - females) / 3 * 1 == money:
                new_solve = males, females, num - males - females
                solve.append(new_solve)
                break

    print('总共有%d个解' % len(solve))
    for i, results in enumerate(solve):  #输出结果的同时知道该结果是列表中的第几个
        print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d' % (i + 1, *results))
##
##    for i in range(results_num - 1):
##        print(solve[i])


def chicken_100_problem_list():
    num, money = 100, 100
    results = [(males, females, num - males - females)
        for males in range(0, num + 1) for females in range(0, num + 1)
            if males * 5 + females * 3 + (num - males - females) / 3 * 1 == money]

    print('总共有%d个解' % len(results))
    for i, result in enumerate(results):
        print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d' % (i + 1, *result))   # *list：序列解包
    #enumerate()

if __name__ == '__main__':
    chicken_100_problem_loop()

    print('-' * 10)

    chicken_100_problem_list()




