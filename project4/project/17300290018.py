#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
编写程序，提示用户输入 pocket 编号，然后显示该 pocket 的颜色，如果用户输入了一
个不在那 37 个编号中的数字，提示错误信息。暂时不考虑用户可能输入的不是整数的情形。
要求采用多分支的选择结构（即 if elif else） 实现。
"""

def get_color(number):
    if number < 0 or number > 36:
        print("编号不在[0,36]")
    elif number == 0:
        print("编号%d的pocket颜色为绿色" % number)
    else:
        if 1<= number <= 10 or 19 <= number <= 28:
            if number % 2 == 0:
                print("编号%d的pocket颜色为黑色" % number)
            else:
                print("编号%d的pocket颜色为红色" % number)
        else:
            if number % 2 == 0:
                print("编号%d的pocket颜色为红色" % number)
            else:
                print("编号%d的pocket颜色为黑色" % number)

def get_color1(number):
    """
    另解：用xor切换0和1
    """
    if number < 0 or number > 36:
        print("编号不在[0,36]")
    elif number == 0:
        print("编号%d的pocket颜色为绿色" % number)
    else:
        flag = (0 if 1 <= number <= 10 or 19 <= number <= 28 else 1) ^ (number % 2)
        color = ["黑色", "红色"]
        print("编号%d的pocket颜色为%s" % (number, color[flag]))

if __name__ == '__main__':
    number = int(input("请输入轮盘赌的pocket编号(0-36)==>"))
    get_color(number)
