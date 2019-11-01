#  -*- coding: utf-8 -*-



if __name__ == '__main__' :
    number = int(input('请输入轮盘赌的一个编号（0-36）==>'))
    if number > 36:
        print('编号不再[0,36]')
    elif number == 0 :
        print('编号%s的pocket颜色为绿色' % number)
    elif number >= 1 and number <= 10:
        if number % 2 == 0 :
            print('编号%s的pocket颜色为黑色' % number)
        else :
            print('编号%s的pocket颜色为红色' % number)
    elif number >= 11 and number <= 18 :
        if number % 2 == 0 :
            print('编号%s的pocket颜色为红色' % number)
        else :
            print('编号%s的pocket颜色为黑色' % number)
    elif number >= 19 and number <= 28 :
        if number % 2 == 0 :
            print('编号%s的pocket颜色为黑色' % number)
        else :
            print('编号%s的pocket颜色为红色' % number)
    elif number >= 29 and number <= 36 :
        if number % 2 == 0 :
            print('编号%s的pocket颜色为红色' % number)
        else :
            print('编号%s的pocket颜色为黑色' % number)
