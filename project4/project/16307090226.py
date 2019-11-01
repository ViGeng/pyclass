#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def main():
    number = int(input("请输入轮盘赌的pocket编号（0-36)==>"))
    if number > 36 or number < 0:
        print ('编号不在[0,36]')
    elif number == 0:
        print ('编号%d的pocket颜色为绿色' % (number))
    elif (number >= 1 and number <=10) or (number >=19 and number <= 28):
        if number % 2 == 0:
            print ('编号%d的pocket颜色为黑色' % (number))
        else:
            print ('编号%d的pocket颜色为红色' % (number))
    else:
        if number % 2 == 0:
            print ('编号%d的pocket颜色为红色' % (number))
        else:
            print ('编号%d的pocket颜色为黑色' % (number))

    


if __name__ == '__main__':
    main()
