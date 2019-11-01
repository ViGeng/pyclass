#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Project 4 轮盘赌颜色
# 宋德夫（17307110044）

def gamble(x):
    if x == 0:
        y = "编号" + str(x) + "的pocket颜色为" + "绿色"
    elif x >= 1 and x <= 10:
        if x % 2 == 0:
            y = "编号" + str(x) + "的pocket颜色为" + "黑色"
        else:
            y = "编号" + str(x) + "的pocket颜色为" + "红色"
    elif x >= 11 and x <= 18:
        if x % 2 == 0:
            y = "编号" + str(x) + "的pocket颜色为" + "红色"
        else:
            y = "编号" + str(x) + "的pocket颜色为" + "黑色"
    elif x >= 19 and x <= 28:
        if x % 2 == 0:
            y = "编号" + str(x) + "的pocket颜色为" + "黑色"
        else:
            y = "编号" + str(x) + "的pocket颜色为" + "红色"
    elif x >= 29 and x <= 36:
        if x % 2 == 0:
            y = "编号" + str(x) + "的pocket颜色为" + "红色"
        else:
            y = "编号" + str(x) + "的pocket颜色为" + "黑色"
    else:
        y = "编号不在[0,36]"
    return y

def main():
    x = input("请输入轮盘赌的pocket编号(0-36)==>")
    x = int(x)
    y = gamble(x)
    print(y)

if __name__ == "__main__":
    main()
        
