#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random

def input_int():
    while True:
        try:
            x = int(input('您猜的数是?'))
            if x < 1 or x > 100:
                print('请输入一个[1,100]范围内的整数')
                continue
            break
        except ValueError as e:
            print('请输入一个[1,100]范围内的整数 {}'.format(e))
    return x

def compare(x, answer):
    result = False
    if x < answer:
        print('您猜的数太小了！')
    elif x > answer:
        print('您猜的数太大了！')
    else:
        print('您猜对了!')
        result = True
    return result

def guess():
    while True:
        answer = random.randint(1,100)
        
        for i in range(4):    
            x = input_int()
            result = compare(x, answer)
            if result:
                break
        
        if not result:
            print('您已经猜了4次，要猜的数是{}'.format(answer))
        
        while True:
            try:
                det = str.lower(input('继续游戏(Y/N)?...'))
                if det not in ('y', 'n'):
                    print('请输入Y/y或N/n')
                    continue
                break
            except ValueError:
                print('请输入Y/y或N/n')
        
        if det == 'n':
            break
if __name__ == '__main__':
    guess()
