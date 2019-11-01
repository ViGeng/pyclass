#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


def main():
    s = int(input("请输入轮盘赌的pocket编号(0-36)==>"))
    if (s >=1 and s<=10) or (s >=19 and s<=28):
        if s % 2 != 0:
            print('编号%d的pocket颜色是红色' %(s))
        else:
            print('编号%d的pocket颜色是黑色' %(s))
    elif s == 0:
        print('编号%d的pocket颜色是绿色' %(s))
    elif ( s >=11 and s<=18) or (s >=29 and s<= 36) :
        if s % 2 != 0:
            print('编号%d的pocket颜色是黑色' %(s))
        else:
            print('编号%d的pocket颜色是红色' %(s))
    else:
        print('编号不在[0,,36]')


if __name__ == '__main__':
    main()
        
            
     

