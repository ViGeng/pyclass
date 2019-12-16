#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random

n=0
randomnumber=random.randint(1,100)
while True: 
    try:
        number=int(input('您猜的数是？'))
        if number<1 or number>100:
            print('请输入一个[1,100]范围的整数')
        if number>=1 and number <=100:
            if number==randomnumber:
                print('您猜对了！')
                choice=input('继续游戏（Y/N）?...')
                if choice=='Y' or choice=='y':
                    n=0
                    randomnumber=random.randint(1,100)
                    continue
                else:
                    quit()                  
            else:
                if number>randomnumber:
                    print('您猜的数太大了！')
                else:
                    print('您猜的数太小了！')
            n+=1
            if n%4==0:
                print('您已经猜了4次了，要猜的数是%d' % (randomnumber))
                choice=input('继续游戏（Y/N）?...')
                if choice=='Y' or choice=='y':
                    n=0
                    randomnumber=random.randint(1,100)
                    continue            
                else:
                    quit()  
    except ValueError as e:
        print('请输入一个[1,100]范围的整数',e)
        n=0
        randomnumber=random.randint(1,100)

        
                      
            
            
            
                
                
                        
        
        
        
    
    
