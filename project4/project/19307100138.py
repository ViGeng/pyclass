#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

def main():
    p=int(input("请输入轮盘赌的pocket编号(0-36)==>"))
    if p<0 or p>36:
         print("编号不在[0,36]")
    elif p<=10:
        if p%2==1:
            print("编号%d的pocket颜色为红色" % p)
        elif p%2==0:
            print("编号%d的pocket颜色为黑色" % p)
    elif p<=18:
        if p%2==1:
            print("编号%d的pocket颜色为黑色" % p)
        elif p%2==0:
            print("编号%d的pocket颜色为红色" % p)
    elif p<=28:
        if p%2==1:
            print("编号%d的pocket颜色为红色" % p)
        elif p%2==0:
            print("编号%d的pocket颜色为黑色" % p)
    elif p<=36:
        if p%2==1:
            print("编号%d的pocket颜色为黑色" % p)
        else:
            print("编号%d的pocket颜色为红色" % p)

if __name__ == '__main__':
  main()


    
