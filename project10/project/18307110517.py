#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
""" project10 猜数游戏
"""

import random


def input_int():
    b1 = input('[1]:您猜的数是？')
    global c
   
    while True:#判断b1是为数字型字符串
        try:
            c = int(b1)
            if c > 100 or c <1:#判断输入的b1不在区间[1,100]内
                print("请输入一个[1,100]范围内的整数")
                b2 = input('[1]:您猜的数是？')
                c = int(b2)
                break
            else:#判断输入的b1在区间[1,100]内
                c = int(b1)
                break
        except ValueError as e:#第一次输入的b1不是数字型字符串，需要再次输入
            print("请输入一个[1,100]范围内的整数invalid literal for int() with base 10:'",b2,"'" )
            x1 = input('[1]:您猜的数是？')
            while True:#判断第二次输入的x1是数字型字符串
                try:
                    c = int(x1)
                except ValueError as e:#判断第二次输入的x1不是数字型字符串，需要再次输入
                    print("请输入一个[1,100]范围内的整数invalid literal for int() with base 10:'",x1,"'" ) 
                    x2 = input('[1]:您猜的数是？')
                    c = int(x2)
                    print("请再次输入上个数")
                    break 
    
def game():
    a = random.randint(1, 100)
    
    if c == a :
        print("您猜对了！")

    else :
        if c > a :
            print("您猜的数太大了！")
        if c < a :
            print("您猜的数太小了!")
        c2 = int(input('[2]:您猜的数是？'))
        if c2 == a :
            print("您猜对了！")

        else:
            if c2 > a:
                print("您猜的数太大了！")
            if c2 < a:
                print("您猜的数太小了!")
            c3 = int(input('[3]:您猜的数是？'))
            if c3 == a:
                print("您猜对了！")

            else:
                if c3 > a:
                    print("您猜的数太大了！")
                if c3 < a:
                    print("您猜的数太小了！")
                c4 = int(input('[4]：您猜的数是？'))
                if c4 == a:
                    print("您猜对了！")
                else:
                    if c4 > a:
                        print("您猜的数太大了！")
                    if c4 < a:
                        print("您猜的数太小了！")
                    print('您已经猜了4次，要猜的数是',a)


if __name__=='__main__':
    input_int()
    game()

    def continue_or_not():
        Z = input("继续游戏？（Y/N）")
        if Z == 'Y' or Z == 'y':
            input_int()
            game()
        else:
            print("游戏结束")
    if __name__ == '__main__':
        continue_or_not()
    

