if __name__ == '__main__':
    a = int(input('请输入轮盘赌的pocket编号(0-36)==>'))
    if a<0 or a>36:
        print('编号不在[0,36]')
    elif a == 0:
        print('编号0的pocket颜色为绿色')
    elif a>=1 and a<=10:
        if a%2 == 1:
            print('编号%d的pocket颜色为红色'%a)
        else:
            print('编号%d的pocket颜色为黑色'%a)
    elif a>=11 and a<=18:
        if a%2 == 1:
            print('编号%d的pocket颜色为黑色'%a)
        else:
            print('编号%d的pocket颜色为红色'%a)
    elif a>=19 and a<=28:
        if a%2 == 1:
            print('编号%d的pocket颜色为红色'%a)
        else:
            print('编号%d的pocket颜色为黑色'%a)
    elif a>=29 and a<=36:
        if a%2 == 1:
            print('编号%d的pocket颜色为黑色'%a)
        else:
            print('编号%d的pocket颜色为红色'%a)
