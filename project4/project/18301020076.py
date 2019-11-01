x = input('请输入轮盘赌的pocket编号（0-36）==>')
x = int(x)

if x<0 or x>36:
    print("编号不在[0,36]")
elif x == 0:
    print("编号为0的pocket颜色为绿色")
elif x<11 or 18<x<29:
    if x % 2 == 1:
        print("编号为"+str(x)+"的pocket颜色为红色")
    else:
        print("编号为"+str(x)+"的pocket颜色为黑色")
elif x<19 or x>28:
    if x % 2 == 1:
        print("编号为"+str(x)+"的pocket颜色为黑色")
    else:
        print("编号为"+str(x)+"的pocket颜色为红色")
