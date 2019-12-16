# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# 猜数游戏 

def game():
    import random
    choice = 'y'
    count = 0
    while choice == 'y' or choice == 'Y':
        num = random.randint(1,100)
        if(count < 4):
            print('您猜的数字是？')
            try:
                guess = int(input())
                if guess < 1 or guess > 100:
                    print('请输入一个[1,100]范围的整数')
                    continue
                count +=1
                if guess < num:
                    print('您猜的数字太小了')
                elif guess > num:
                    print('您猜的数字太大了')
                else:
                    print('您猜对了!')
                    count = 0
                    print('继续游戏(Y/N)?')
                    choice = input()
            except Exception as e:
                print('请输入一个[1,100]范围的整数',e)
                continue
        else:
            print('您已经猜了4次，要猜的数字是',num)
            count = 0
            print('继续游戏(Y/N)?')
            choice = input()


if __name__=='__main__':
    game()
