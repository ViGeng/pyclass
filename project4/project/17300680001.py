#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def which_color(number):
    if number == 0:
        return '绿色'
    elif number >= 1 and number <= 10 or number >= 19 and number <=28:
        if number % 2 == 1:
            return '红色'
        else:
            return '黑色'
    else:
        if number % 2 == 1:
            return '黑色'
        else:
            return '红色'

if __name__ == '__main__':
    number = int(input('请输入轮盘赌的pocket编号(0-36)==>'))
    result = which_color(number)
    if number < 0 or number > 36:
        print('编号不在[0，36]')
    else:
        print('%s%d%s%s' %('编号',number,'的pocket颜色为',result))
    
    
