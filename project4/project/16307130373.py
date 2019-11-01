#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def corona_color(number):
    if number<0 or number>36:
        result = '编号不在[0，36]'
    elif number < 1:
        result = '绿色'
    elif number < 11:
        if (number % 2) == 1:
            result = '红色'
        else:
            result = '黑色'
    elif number < 19:
        if (number % 2) == 1:
            result = '黑色'
        else:
            result = '红色'
    elif number < 29:
        if (number % 2) == 1:
            result = '红色'
        else:
            result = '黑色'
    else:
        if (number % 2) == 1:
            result = '黑色'
        else:
            result = '红色'
    return result


if __name__=='__main__':
    number = int(input("请输入轮盘赌的pocket编号（0-36)==>"))
    result = corona_color(number)
    if len(result) == 2:
        print('编号%d的pocket颜色为%s'%(number,result))
    else:
        print('%s'%result)
##    test = range(-2,42)
##    for i in test:
##        result = corona_color(i)
##        if len(result) < 3:
##           print('编号%d的pocket颜色为%s'%(i,result))
##        else:
##           print('%s'%result)
        


        
        
