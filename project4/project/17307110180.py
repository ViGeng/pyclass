number = input("请输入轮盘赌的pocket编号(0-36)==>")
if int(number) == 0:
    print("编号0的pocket颜色为绿色")
elif 1 <= int(number) <=10:
    if int(number)%2 ==0:
        print("编号" + number + "的pocket颜色为黑色")
    else:
        print("编号" + number + "的pocket颜色为红色")
elif 11 <= int(number) <=18:
    if int(number)%2 ==0:
        print("编号" + number + "的pocket颜色为红色")
    else:
        print("编号" + number + "的pocket颜色为黑色")
elif 19 <= int(number) <=28:
    if int(number)%2 ==0:
        print("编号" + number + "的pocket颜色为黑色")
    else:
        print("编号" + number + "的pocket颜色为红色")
elif 29 <= int(number) <=36:
    if int(number)%2 ==0:
        print("编号" + number + "的pocket颜色为红色")
    else:
        print("编号" + number + "的pocket颜色为黑色")   
else:
    print("编号不在[0,36]")
