#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import random


def guess(count):
    while True:
        try:
            input_1 = input('[%d]:您猜的数是？' % count)
            guess = int(input_1)
        except ValueError as e:
            print('请输入一个[1,100]范围内的整数\t%s' %
                  (e))
        else:
            if guess in range(1,101):
                break
            else:
                print('请输入一个[1,100]范围内的整数')
    return guess


def game():
    answer = random.randint(1,100)
    count = 0
    while True:
        if count >= 4:
            print('您已经猜了4次，要猜的数是%d' % answer)
            input_2 = input('继续游戏(Y/N)?...')
            if input_2 in ['y','Y']:
                count = 0
                answer = random.randint(1,100)
                continue
            elif input_2 in ['n','N']:
                break
            else:
                raise Exception('请输入Y/N')
        count += 1
        guess_num = guess(count)
        if guess_num == answer:
            print('恭喜您猜对了~')
            break
        elif guess_num > answer:
            print('您猜的数太大了！')
        elif guess_num < answer:
            print('您猜的数太小了！')
            

    
if __name__ == '__main__':
    game()
