#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import random
count = 0
while(1):
    real_number = random.randint(1,100)
    while(1):
        try:
            number = int(input('您猜的数是？'))
            if(number>100 or number<1):
                print('请输入一个[1,100]范围的整数')
                continue
            else:
                if(number>real_number):
                    print('您猜的数太大了！')
                    count+=1
                    if(count>=4):
                        print('您已经猜了4次，要猜的数是%d',real_number)
                        break
                elif(number<real_number):
                    print('您猜的数太小了！')
                    count+=1
                    if(count>=4):
                        print('您已经猜了4次，要猜的数是%d'%(real_number))
                        break
                else:
                    print('您猜对了')
                    break
        except Exception as err:
            print('请输入一个[1,100]范围的整数 '+str(err))
    continue_game = input('继续游戏（Y/N）?')
    if(continue_game.lower()=='y'):
        continue
    else:
        break
            
        