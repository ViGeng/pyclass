#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


def result(num):
    if num == 0:
        color = '绿'
    elif (num >=1 and num <= 10) or (num >=19 and num <=28):    #用 in range()语句 需要逻辑转换（开闭集），可读性差！
        if num % 2 == 1:
            color = '红'
        else:
            color = '黑'
    elif (num >=11 and num <= 18) or (num >=29 and num <=36):
        if num % 2 == 1:
            color = '黑'
        else:
            color = '红'
    return(color)

if __name__ == '__main__':

    num = int(input('请输入轮盘赌的pocket编号（0-36）==>'))
    if num >= 0 and num <= 36:
        color = result(num)
        print('编号%s的pocket颜色为%s色' % (num, color))
    else:
        print('编号不在[0,36]')







