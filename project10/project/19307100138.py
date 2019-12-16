#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

import random
set_number=random.randint(0,100)
guess_number=input("[1]:您猜的数是？")
while True:
    try:
         guess_number=int(guess_number)
    except NameError:
        print("请输入一个[1,100]范围的整数 invalid literal for int()with base 10")
    except ValueError:
        print("请输入一个[1,100]范围的整数")
    except guess_number<0:
        print("请输入一个[1,100]范围的整数")
        if guess_number>0:
            break
    else:
        if int(guess_number)>0:
            break
for guess_number in (0,100):
    icount=1
    if guess_number==set_number:
        print("您猜对了！")
    while guess_number!=set_number:
        if guess_number>set_number:
            step=input("您猜的数字太大了!\n[%d]:您猜的数是？"%(icount+1))
        else:
            step=input("您猜的数字太小了!\n[%d]:您猜的数是？"%(icount+1))
        icount=icount+1
        guess_number=int(step)
        if guess_number==set_number:
            print("您猜对了！")
        while icount>3:
            if guess_number==set_number:
                print("您猜对了！")
            else:
                print("您已经猜了4次，要猜的数是%d"%set_number)
                quit()
n=input("继续游戏(Y/N)?...")
if n=="y" or "Y":
    print("[1]:您猜的数是？")
else:
    quit()
        


    
