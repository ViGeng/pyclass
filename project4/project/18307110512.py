#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

if __name__=='__main__':
    num=int(input('请输入轮盘赌的pocket编号(0-36)==>'))

if num > 36 or num < 0:
    print('编号不在[0,36]')

else:
    if num == 0:
        print('编号为',num,'的pocket颜色为绿色',sep='')
    else:
        if num <= 10:
            if num % 2 == 1:
                print('编号为',num,'的pocket颜色为红色',)
            else:
                print('编号为',num,'的pocket颜色为黑色',sep='')
        else:
            if num <= 18:
                if num % 2 == 1:
                    print('编号为',num,'的pocket颜色为黑色',sep='')
                else:
                    print('编号为',num,'的pocket颜色为红色',sep='')
            else:
                if num <= 28:
                    if num % 2 == 1:
                        print('编号为',num,'的pocket颜色为红色',sep='')
                    else:
                        print('编号为',num,'的pocket颜色为黑色',sep='')
                else:
                    if num <= 36:
                        if num % 2 == 1:
                            print('编号为',num,'的pocket颜色为黑色',sep='')
                        else:
                            print('编号为',num,'的pocket颜色为红色',sep='')



