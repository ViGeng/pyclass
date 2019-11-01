#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

def pocket(number):
    if number > 36 or number < 0:
        return '编号不在[0,36]'
    elif number == 0:
        return '编号0的pocket颜色为绿色'
    elif 1 <= number <= 10 or 19 <= number <= 28:
        if number % 2 == 1:
            return '编号%d的pocket颜色为红色'%number
        else:
            return '编号%d的pocket颜色为黑色'%number
    elif 11 <= number <= 18 or 29 <= number <= 36:
        if number % 2 == 1:
            return '编号%d的pocket颜色为黑色'%number
        else:
            return '编号%d的pocket颜色为红色'%number
        
def main():
    number = int( input('请输入轮盘赌的pocket编号(0-36)==>') )
    print( pocket(number) )

if __name__ == '__main__':
    main()
