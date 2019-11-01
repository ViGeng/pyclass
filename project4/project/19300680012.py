from math import *
num=int(input("请输入轮盘赌的pocket编号(0-36)==>"))
if num>=37 or num<0:
    print("编号不在[0,36]")
elif num>=29:
    if num %2==0:
        print("编号为%d的pocket颜色为红色"%num)
    else:
        print("编号为%d的pocket颜色为黑色"%num)
elif num>=19:
    if num %2==1:
        print("编号为%d的pocket颜色为红色"%num)
    else:
        print("编号为%d的pocket颜色为黑色"%num)
elif num>=11:
    if num %2==0:
        print("编号为%d的pocket颜色为红色"%num)
    else:
        print("编号为%d的pocket颜色为黑色"%num)
elif num>=1:
    if num %2==1:
        print("编号为%d的pocket颜色为红色"%num)
    else:
        print("编号为%d的pocket颜色为黑色"%num)
else:
    print("编号为%d的pocket颜色为绿色"%num)

