#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#Project10 作者：19级经济学院 应眺

import random

def guess(counter):
    while True:
        try:
            n = int(input('[%s]Input youe answer here'%counter))
        except Exception:
            print('please input an integer from 1 to 100')
        else:
            if  not n in range(1,101):
                print('please input an integer from 1 to 100')
            else:
                return n

def judge():
    input('Press Enter to start the game')
    rannum = random.randint(1,100)
    counter = 0
    while True:
        counter += 1
        if counter > 4:
            print('You lose! The correct answer is %i'%rannum)
            counter = 0
            if input('Continue(Y/N)?') in 'Yy':
                rannum = random.randint(1,100)
                continue
            else:
                return
        else:
            n = guess(counter)
            if n > rannum:
                print('Your answer is too big!')
            elif n < rannum:
                print('Your answer is too small!')
            else:
                print('You win!')
                counter = 0
                if input('Continue(Y/N)?') in 'Yy':
                    rannum = random.randint(1,100)
                    continue    
                else:
                    return
                
if __name__ == '__main__':
    judge()
exit()
