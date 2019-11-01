a=input("请输入轮盘赌的pocket编号（0—36）==>")
if 0<=int(a)<=36:
    if 1<=int(a)<=10:
        if int(a)%2==0:
            print("编号为",a,"的pocket颜色为黑色")
        else:
            print("编号为",a,"的pocket颜色为红色")
    if 11<=int(a)<=18:
        if int(a)%2==0:
            print("编号为",a,"的pocket颜色为红色")
        else:
            print("编号为",a,"的pocket颜色为黑色")
    if 19<=int(a)<=28:
        if int(a)%2==0:
            print("编号为",a,"的pocket颜色为黑色")
        else:
            print("编号为",a,"的pocket颜色为红色")
    if 29<=int(a)<=36:
         if int(a)%2==0:
            print("编号为",a,"的pocket颜色为红色")
         else:
            print("编号为",a,"的pocket颜色为黑色")
    if int(a)==0:
        print("编号为0的pocket颜色为绿色")
else:
    print("编号不在[0—36]")
    
