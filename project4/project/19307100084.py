s=int(input("请输入轮盘赌的pocket编号(0-36)==>"))

if s<=36:
    if s==0:
       print('编号为0的pocket颜色为绿色')
    elif s>= 1 and s<= 10:
        if s%2 == 0:
            print('编号',s,'的pocket颜色为黑色')
        else:
            print('编号',s,'的pocket颜色为红色')
    elif s>= 11 and s<= 18:
        if s%2 == 0:
            print('编号',s,'的pocket颜色为红色')
        else:
            print('编号',s,'的pocket颜色为黑色')
    elif s>= 19 and s<= 28:
        if s%2 == 0:
            print('编号',s,'的pocket颜色为黑色')
        else:
            print('编号',s,'的pocket颜色为红色')
    elif s>=29 and s<=36:
        if s%2 == 0:
            print('编号',s,'的pocket颜色为红色')
        else:
            print('编号',s,'的pocket颜色为黑色')
else:
    print('编号不在[0,36]')
