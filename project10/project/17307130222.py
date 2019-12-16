#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
# File     : 17307130222_pj10.py

# Author   : Zhukaixiang 17307130222

# Date     : 2019/12/11

def NumGuess():
    import random
    num=random.randint(1,100)
    found = False
    i=0
    while not found:        
        try:
            x=int(input('[%d]:您猜的数是？' %(i+1)))
            if 0 <= x <= 100 :
                i += 1
                if x < num:
                    print('您猜的数太小了！')
                elif x > num:
                    print('您猜的数太大了！')
                elif x == num:
                    print('您猜对了')
                    order=input('继续游戏(Y/N)?')
                    if order == 'Y' or order == 'y':
                        NumGuess()
                    elif order == 'N' or order == 'n':
                        found = True
                        break
            else:
                print('请输入一个[1,100]范围的整数')
        except ValueError as e:
            print('请输入一个[1,100]范围内的整数 %s' %e)
        if i == 4:
            print('您已经猜了4次了，要猜的数是%d' %num)
            order=input('继续游戏(Y/N)?')
            if order == 'Y' or order == 'y':
                NumGuess()
            elif order == 'N' or order == 'n':
                found = True

if __name__=='__main__':
    NumGuess()
    
        
