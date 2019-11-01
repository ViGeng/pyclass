#!/usr/bin/env python

# -*- coding: utf-8 -*-

# File     : 17307130222_pj4.py

# Author   : Zhukaixiang 17307130222

# Date     : 2019/10/29


n = int(input('请输入轮盘赌的pocket编号(0-36)==>'))

if n > 36 or n < 0 :
    print('编号不在[0,36]')
elif n == 0 :
    print('编号为0的pocket颜色为绿色')
elif( n >= 1 and n <= 10 ) or ( n >= 19 and n <= 28 ):
    if n % 2 :
        print('编号为%d的pocket颜色为红色' %n)
    else:
        print('编号为%d的pocket颜色为黑色' %n)
elif( n >= 11 and n <= 18 ) or( n >= 29 and n <= 36):
    if n % 2 :
        print('编号为%d的pocket颜色为黑色' %n)
    else:
        print('编号为%d的pocket颜色为红色' %n)
