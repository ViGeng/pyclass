#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


import random

def main():
    again = 'Y'
    while again == 'Y' or again == 'y':
        key = random.randint(1,101)
        counter = 1
        while counter <= 4:
            try:
                number = int(input('[%d]您猜的数是？'%(counter)))
                if 1 <= number <= 100:
                    if number == key:
                        print('您猜对了！')
                        break
                    elif number < key:
                        print('您猜的数太小了！')
                        counter += 1
                    else:
                        print('您猜的数太大了！')
                        counter += 1
                else:
                    print('请输入一个[1,100]范围的整数')
            except Exception as e:
                    print('请输入一个[1,100]范围的整数',e)
        if counter == 5:
            print('您已经猜了4次，要猜的数是%d' %(key))
        again = input('继续游戏(Y/N)?...')

if __name__ == '__main__':
    main()


