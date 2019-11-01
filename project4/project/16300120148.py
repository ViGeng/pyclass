pocket=int(input("请输入轮盘赌的pocket编号(0-36)==>"))
if(pocket==0):
    print("编号{}的pocket颜色为绿色".format(pocket))
elif(1<=pocket and pocket<=10):
    if(pocket%2==0):
        print("编号{}的pocket颜色为黑色".format(pocket))
    else:
        print("编号{}的pocket颜色为红色".format(pocket))
elif(11<=pocket and pocket<=18):
    if(pocket%2==0):
        print("编号{}的pocket颜色为红色".format(pocket))
    else:
        print("编号{}的pocket颜色为黑色".format(pocket))
elif(19<=pocket and pocket<=28):
    if(pocket%2==0):
        print("编号{}的pocket颜色为黑色".format(pocket))
    else:
        print("编号{}的pocket颜色为红色".format(pocket))
elif(29<=pocket and pocket<=36):
    if(pocket%2==0):
        print("编号{}的pocket颜色为红色".format(pocket))
    else:
        print("编号{}的pocket颜色为黑色".format(pocket))
else:
    print("编号不在[0,36]")