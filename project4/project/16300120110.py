#! /usr/bin/env python3
#  -*- coding: utf-8 -*-



def main ():
    a = int ( input ( "请输入轮盘赌的pocket编号(0-36)==>" ))

    if not ( 0 <= a <= 36 ):
        print ( "编号不在[0,36]" )
    elif a == 0:
        print ( "编号%a的pocket颜色为绿色" % (a))
    elif ( 0 < a <= 10 ) or ( 19 <= a <= 28 ):
        if ( a % 2 == 0 ):
            print ( "编号%a的pocket颜色为黑色" % (a))
        else :
            print ( "编号%a的pocket颜色为红色" % (a))
    elif ( a % 2 == 0 ): 
        print ( "编号%a的pocket颜色为红色" % (a))
    else :
            print ( "编号%a的pocket颜色为黑色" % (a))
            

if __name__ == '__main__':
    main ()
    
