#! /usr/bin/env python4
#  -*- coding: utf-8 -*-


""" 下面的一段代码提示用户输入pocket编号0-36，显示该pocket颜色。
    如果用户输入不在那37个编号中的数字，提示错误信息。
"""

number = int(input('请输入轮盘赌赌pocket编号(0-36)==>'))
if number == 0:
        print('编号%s的pocket颜色为绿色'%number)
elif 1 <= number <= 10:
    if number % 2 != 0:
        print('编号%s的pocket颜色为红色'%number)
    else:
        print('编号%s的pocket颜色为黑色'%number)
elif 11 <= number <= 18:
    if number % 2 != 0:
        print('编号%s的pocket颜色为黑色'%number)
    else:
        print('编号%s的pocket颜色为红色'%number)
elif 19 <= number <= 28:
    if number % 2 != 0:
        print('编号%s的pocket颜色为红色'%number)
    else:
        print('编号%s的pocket颜色为黑色'%number)
elif 29 <= number <= 36:
    if number % 2 != 0:
        print('编号%s的pocket颜色为黑色'%number) 
    else:
        print('编号%s的pocket颜色为红色'%number) 
else:
    print('编号不在[0-36]')
            

if __name__ == 'main':
    main()           
