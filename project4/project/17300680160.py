print("请输入轮盘赌的pocket编号（0-36）==>",end="")
a_str = input()
a = int(a_str)
if a>36:
    print("编号不在[0,36]")
elif a>=29:
    if a%2==0:
        print("编号为%d的pocket颜色为红色" % a)
    else :
        print("编号为%d的pocket颜色为黑色" % a)
elif a>=19:
    if a%2==0:
        print("编号为%d的pocket颜色为黑色" % a)
    else :
        print("编号为%d的pocket颜色为红色" % a)
elif a>=11:
    if a%2==0:
        print("编号为%d的pocket颜色为红色" % a)
    else :
        print("编号为%d的pocket颜色为黑色" % a)
elif a>=1:
    if a%2==0:
        print("编号为%d的pocket颜色为黑色" % a)
    else :
        print("编号为%d的pocket颜色为红色" % a)
elif a==0:
    print("编号为0的pocket颜色为绿色")
else :
    print("编号不在[0,36]")
