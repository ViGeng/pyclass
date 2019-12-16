#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import random

def gueessnumber_game(flag='Y'):
    while flag == 'Y' or flag == 'y':
        times = 1
        guess_number = 0
        number  = random.randint(1, 100)

        #print("要猜的数是{}".format(number))
        
        
        while times<= 4:
            guess = input("{}:您猜的数是".format(times))
            try:               
                guess_number = int(guess)          
                if 1 <= guess_number <=100:
                    times  = times + 1
                    if guess_number == number:  
                        print("您猜对了！")
                        break
                    elif guess_number > number:
                        print("您猜的数太大了！")
                    else:
                        print("您猜的数太小了！")
                else:
                    print("请输入一个[1,100]范围的整数") 
            except ValueError as e:
                    print("请输入一个[1,100]范围的整数 invalid literal for int() with base 10: '{:s}'".format(guess))
        if times == 5:
            print("您已经猜了4次，要猜的数是{}".format(number))

        flag = input("继续游戏(Y/N)？")
    
                    
if __name__ == '__main__':
    gueessnumber_game()
    
                            
            
