#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-


def color1(pocket):
    if pocket % 2 == 0:
        return '黑'
    else:
        return '红'


def color2(pocket):
    if pocket % 2 == 0:
        return '红'
    else:
        return '黑'


def main(): 
    pocket = int(input('请输入轮盘赌的pocket编号（0-36）==>'))
    if pocket == 0:
        print('编号0的pocket颜色为绿色')
    else:
        if pocket < 0 or pocket > 36:
            print('编号不在[0,36]')
        else:
            if pocket < 11:
                pocketcolor = color1(pocket)
            else:
                if pocket < 19:
                    pocketcolor = color2(pocket)
                else:
                    if pocket < 29:
                        pocketcolor = color1(pocket)
                    else:
                        pocketcolor = color2(pocket)
            print('编号%d的pocket颜色为%s色' % (pocket,pocketcolor))


if __name__ == '__main__':
    main()
