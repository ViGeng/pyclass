#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


x=int(input("请输入轮盘赌的pocket编号(0-36)==>"))
if x<0 or x>36:
    print("编号不在[0,36]")
elif (x>=1 and x<=10) or (x>=19 and x<=28):
    if x%2==0:
        print("编号%d的pocket颜色为黑色" % x)
    else:
        print("编号%d的pocket颜色为红色" % x)
else:
    if x%2==0:
        print("编号%d的pocket颜色为红色" % x)
    else:
        print("编号%d的pocket颜色为黑色" % x)


