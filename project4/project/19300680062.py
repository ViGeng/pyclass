#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#Project4 作者：19级经济学院 应眺
def game():
    n = input('请输入轮盘赌的pocket编号(0-36)')
    n = int(n)
    if n < 0 or n > 36:
        print('编号不在[0,36]')
    else:
        if n == 0:
            color = '绿色'
        elif n <= 10:
            if n % 2 == 1:
                color = '红色'
            else:
                color = '黑色'
        elif n <= 18:
            if n % 2 == 1:
                color = '黑色'
            else:
                color = '红色'
        elif n <= 28:
            if n % 2 == 1:
                color = '红色'
            else:
                color = '黑色'
        else:
            if n % 2 == 1:
                color = '黑色'
            else:
                color = '红色'
        print('编号%i的pocket颜色为%s'%(n, color))
    game()
                
if __name__ == '__main__':
    game()
