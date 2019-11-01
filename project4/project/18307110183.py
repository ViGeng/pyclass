#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def pocket_color_1(code):
    if (code >= 0 and code <= 36):
        answer = '编号%d的pocket颜色是%s' % (code,pocket_color_2(code))
    else:
        answer = '编号不在[0,36]'
    return answer


def pocket_color_2(code):
    color = ['绿色','红色','黑色']
    if code == 0:
        color_num = 0
    elif code >= 1 and code <= 10:
        if code % 2 == 1:
            color_num = 1
        else:
            color_num = 2 
    elif code >= 11 and code <= 18:
        if code % 2 == 1:
            color_num = 2
        else:
            color_num = 1
    elif code >= 19 and code <= 28:
        if code % 2 == 1:
            color_num = 1
        else:
            color_num = 2
    else:
        if code % 2 == 1:
            color_num = 2
        else:
            color_num = 1
    color_name = color[color_num]
    return color_name


if __name__ == '__main__':

    pocket_code = int(input('请输入轮盘赌的pocket编号（0-36）==>'))
    print(pocket_color_1(pocket_code))
