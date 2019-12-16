#!/usr/bin/env python3
#  -*- coding: utf-8 -*-#

'''编写一个猜数游戏， 计算机随机产生一个[1,100]范围内的数，用户可以有最多 4 次机会来
猜数， 如果猜的数大或者小时都应该提示用户猜的数是偏大还是偏小。如果在机会用完之
前猜对或者 4 次机会用完但未猜对， 该局游戏都会结束。询问用户是否继续新的游戏，回
答 Y/y 时继续，否则退出。在用户猜数过程中要能够处理用户输入异常的情况。'''


import random

def guess_number():

    while True: #new_game == True:                               #新一轮游戏

        '''初始化'''
        correct_num = random.randint(1,100)                      #初始化
        #print(correct_num)                                      #测试是否真的“猜对”
        guess_time = 0

        while guess_time < 4:                                    #猜4次
            guess_time = guess_time + 1

            '''异常处理部分'''
            while True:                                                                    #while True 语句，当输入符合需求后即break
                try:
                    user_num = int(input('[{}]: 您猜的数是？'.format(guess_time)))          #把输入内容放在测试中
                    if  user_num < 1 or user_num > 100:                                     #超出范围数字异常
                        print('超出范围，请输入一个[1,100]范围内的整数')
                    else:
                        break                                                               #内容合法且在范围内后就退出while True循环
                except ValueError as e:                                                        #非数字异常
                        print('请输入一个[1,100]范围内的整数 {}'.format(e))

            '''正常猜数游戏  流程'''
            if user_num == correct_num:                                              #猜数游戏流程
                print('您猜对了！')
                guess_time = 4
            else:
                guess_error = '大'
                if user_num < correct_num:
                    guess_error = '小'
                print('您猜的数太{}了！'.format(guess_error))

        if user_num != correct_num:
            print('您已经猜了{}次，要猜的数是 {}'.format(guess_time, correct_num))

        question = input('继续游戏（Y/N）？...')
        if question in ('Y', 'y'):
            continue
        else:
            break

    print('游戏结束')

    pass


if __name__ == '__main__':
    guess_number()
