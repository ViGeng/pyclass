#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-


def output(list_):
    print('总共有%d个解' % len(list_))
    for i in range(len(list_)):
        print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d' % (i+1, list_[i][0], list_[i][1], list_[i][2]))
    print()   
        


##第一种采用循坏结构的方法
def main1():
    answer1 = []
    for rooster in range(21):
        for hen in range(34):
            chicken = 100 - rooster - hen
            if rooster * 5 + hen * 3 + chicken / 3 == 100:
                answer1.append([rooster, hen, chicken])
    output(answer1)



##第二种采用列表解析式的方法
def main2():
    answer2 = [[rooster, hen, 100 - rooster - hen] for rooster in range(21) \
               for hen in range(34) if rooster * 5 + hen * 3 + \
               (100 - rooster - hen) / 3 == 100]
    output(answer2)



if __name__ == '__main__':
    main1()
    main2()
