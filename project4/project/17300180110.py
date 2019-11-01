number=int(input('请输入轮盘赌的pocket编号（0—36）==>'))

if number>36:
    print('编号不在[0,36]')
else:
    if number%2==0:
        if number==0:
            print('绿色')
        elif number>=29:
            print('红色')
        elif number>=19:
            print('黑色')
        elif number>=11:
            print('红色')
        else:
            print('黑色')
    else:
        if number>=29:
            print('黑色')
        elif number>=19:
            print('红色')
        elif number>=11:
            print('黑色')
        else:
            print('红色')

