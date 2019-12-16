#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
编写一个猜数游戏， 计算机随机产生一个[1,100]范围内的数，用户可以有最多 4 次机会来
猜数， 如果猜的数大或者小时都应该提示用户猜的数是偏大还是偏小。如果在机会用完之
前猜对或者 4 次机会用完但未猜对， 该局游戏都会结束。询问用户是否继续新的游戏，回
答 Y/y 时继续，否则退出。在用户猜数过程中要能够处理用户输入异常的情况。
"""

import random

def input_number(try_times):
    while True:
        number = input("[{:d}]:您猜的数是？".format(try_times))
        try:
            number = int(number)
            if 1 <= number <= 100:
                return number
            else:
                print("请输入一个[1,100]范围的整数")
        except ValueError as e:
            print("请输入一个[1,100]范围的整数 invalid literal for int() with base 10: '{:s}'".format(number))

def guess():
    try_times = 1
    answer = random.randint(1, 100)
    while try_times <= 4:
        number = input_number(try_times)
        if number == answer:
            return True, None
        else:
            try_times += 1
            if number > answer:
                print("您猜的数太大了！")
            else:
                print("您猜的数太小了！")
    return False, answer
            
def main():
    flag = 'Y'
    while flag == 'Y' or flag == 'y':
        correct, answer = guess()
        if correct:
            print("您猜对了！")
        else:
            print("您已经猜了4次，要猜的数是{:d}".format(answer))
        flag = input("继续游戏(Y/N)？")
        
if __name__ == '__main__':
    main()
