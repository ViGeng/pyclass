#! /usr/bin/env python3
# -*- coding: utf-8 -*-

number = int(input('请输入轮盘赌的pocket编号（0—36）==>'))


if number > 37 or number <0:
    print('编号不在[0,36]')
elif number == 0:
    print('编号',number,'的pocket颜色为绿色',sep='')
elif 0 < number < 11 or 18 < number < 29:
    if number % 2 == 0:
        print('编号',number,'的pocket颜色为黑色',sep='')
    else:
         print('编号',number,'的pocket颜色为红色',sep='')
elif 10 < number < 19 or 28 < number <37:
    if number % 2 == 0:
        print('编号',number,'的pocket颜色为红色',sep='')
    else:
         print('编号',number,'的pocket颜色为黑色',sep='')




