# -*- coding: utf-8 -*-
 

num = int(input("请输入轮盘赌的pocket编号（0-36）==>"))
    
if num==0:
        print("pocket颜色为绿色")
elif num>=1 and num<=10:
    if num%2==0: print("pocket颜色为黑色")
    else: print("pocket颜色为红色")
elif num>=11 and num<=18:
    if num%2==0: print("pocket颜色为红色")
    else: print("pocket颜色为黑色")
elif num>=19 and num<=28:
    if num%2==0: print("pocket颜色为黑色")
    else: print("pocket颜色为红色")
elif num>=29 and num<=36:
    if num%2==0: print("pocket颜色为红色")
    else: print("pocket颜色为黑色")
else:
        print("编号不在[0,36]")

