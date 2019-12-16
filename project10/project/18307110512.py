#! /usr/bin/env python3
#! -*- coding:utf8 -*-

import random

def game():
    right_num = random.randint(1,100)
    for i in range(4):
        while True:
            try:
                y = input('[%d]:您猜的数是？'%(i+1))
                guess_num = eval(y)
                if guess_num not in range(1,101):
                    print('请输入一个[1,100]范围的整数')
                    continue
                break
            except:
                print('请输入一个[1,100]范围的整数 invalid literal for int() with base 10: \'{:}\''.format(y))
        if guess_num < right_num:
            print('您猜的数太小了！')
            if i == 3:
                print('您已经猜了4次，要猜的数是{0}'.format(right_num))
            continue
        elif guess_num > right_num:
            print('您猜的数太大了！')
            if i == 3:
                print('您已经猜了4次，要猜的数是{0}'.format(right_num))
            continue
        else:
            print('您猜对了！')
            break

def main():
    game()
    while True:
        go_on = input('继续游戏(Y/N)?...')
        if go_on is 'Y' or 'y':
            game()
        else:
            break

if __name__ == '__main__':
    main()
