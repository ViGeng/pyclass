#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

if __name__ == '__main__':
    list = ['绿色', '红色', '黑色']
    i = int(input('请输入轮盘赌的pocket编号(0-36)==>'))
    i_mod = i % 2

    if i in range(37):
        if i == 0:
            out = list[0]
        elif ((i >= 1) and (i <= 10)) or ((i >= 19) and (i <= 28)):
            if i_mod == 1:
                out = list[1]
            else:
                out = list[2]
        elif ((i >= 11) and (i <= 18)) or ((i >= 29) and (i <= 36)):
            if i_mod == 1:
                out = list[2]
            else:
                out = list[1]
        print('编号%d的pocket颜色为%s' % (i, out))
    else:
        print('编号不在[0, 36]')


    
