#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Project 6 百鸡问题
# 宋德夫（17307110044）

def the_chicken_problem_1():
    list1 = []
    for chick in range(0, 100 + 1):
        if chick % 3 == 0:
            for hen in range(0, 100 - chick + 1):
                cock = 100 - chick - hen
                if cock * 5 + hen * 3 + chick / 3 == 100:
                    list1.append("鸡翁 " + str(cock) +
                                 " 鸡母 " + str(hen) +
                                 " 鸡雏 " + str(chick))
    print("总共有" + str(len(list1)) + "个解")
    for number in range(1, len(list1) + 1):
        print("解" + str(number) + ":" + list1[number - 1])

def the_chicken_problem_2():
    list2 = ["鸡翁 " + str(100 - chick - hen) + " 鸡母 " + str(hen) +
             " 鸡雏 " + str(chick) for chick in range(0, 100 + 1)
             if chick % 3 == 0 for hen in range(0, 100 - chick + 1)
             if (100 - chick - hen) * 5 + hen * 3 + chick / 3 == 100]
    print("总共有" + str(len(list2)) + "个解")
    for number in range(1, len(list2) + 1):
        print("解" + str(number) + ":" + list2[number - 1])
    
def main():
    the_chicken_problem_1()
    print('-' * 40)
    the_chicken_problem_2()

if __name__ == "__main__":
    main()
