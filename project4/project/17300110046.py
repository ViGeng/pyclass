x = eval(input('请输入轮盘赌的pocket编号(0-36)==>'))
if type(x) == int:
    if 0 <= x <= 36:
        if x==0:
            print('编号为%d的pocket颜色为绿色'%x)
        elif 1 <= x <= 10:
            if x % 2 != 0:
                print('编号为%d的pocket颜色为黑色'%x)
            else:
                print('编号为%d的pocket颜色为红色'%x)
    elif 11 <= x <= 18:
        if x % 2 != 0:
            print('编号为%d的pocket颜色为红色'%x)
        else:
            print('编号为%d的pocket颜色为黑色'%x)
    elif 19 <= x <= 28:
        if x % 2 != 0:
            print('编号为%d的pocket颜色为黑色'%x)
        else:
            print('编号为%d的pocket颜色为红色'%x)            
    elif 29 <= x <= 36:
        if x % 2 != 0:
            print('编号为%d的pocket颜色为红色'%x)
        else:
            print('编号为%d的pocket颜色为黑色'%x)
    else:
        print('编号不在[0,36]')
