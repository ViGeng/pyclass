#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
'''
    猜数游戏：输入一个相应范围内的整数，有四次机会来猜数，四次没猜中游戏结束，询问是否继续
'''

import random


def main():
    _range = 100  #输入猜数游戏的范围
    i = 1
    answer = random.randint(1,_range+1)
    decide = False  #决定是否继续游戏
    while True:
        if i > 4:
            if not decide:
                    print('您已经猜了4次，要猜的数是%d' % answer)
            next_run = str(input('继续游戏(Y/N)'))
            if next_run.strip().lower() == 'y':
                i = 1
                answer = random.randint(1,_range+1)
                decide = False
                continue

            else:
                if next_run.strip().lower() == 'n':
                    break
                else:
                    print('请输入Y或者N')
                    decide = True
                    continue
            
        try:
            text = input('[%d]:你猜的数是？' % i)
            n = int(text)
        except Exception as e:
            print('请输入一个[1，{}]的整数 {}'.format(_range,e))
            continue
        if n<1 or n>_range :
            print('请输入一个[1，%d]的整数' % _range)
            continue
        else:
            if n == answer:
                print('您猜对了！')
                break
            else:
                if n > answer:
                    print('您猜的太大了！')
                    i += 1
                    continue
                else:
                    if n < answer :
                        print('您猜的太小了！')
                        i += 1
                        continue


if __name__ == '__main__':
    main()
