def pocket_num():
    num_int = int(num)
    if num_int == 0:
        print('编号%d的pocket颜色为绿色' % (num_int))
    elif num_int <= 10:
        if num_int % 2 == 0:
            print('编号%d的pocket颜色为黑色' % (num_int))
        else:
            print('编号%d的pocket颜色为红色' % (num_int))
    elif num_int <= 18:
        if num_int % 2 == 0:
            print('编号%d的pocket颜色为红色' % (num_int))
        else:
            print('编号%d的pocket颜色为黑色' % (num_int))
    elif num_int <= 28:
        if num_int % 2 == 0:
            print('编号%d的pocket颜色为黑色' % (num_int))
        else:
            print('编号%d的pocket颜色为红色' % (num_int))
    elif num_int <= 36:
        if num_int % 2 == 0:
            print('编号%d的pocket颜色为红色' % (num_int))
        else:
            print('编号%d的pocket颜色为黑色' % (num_int))
    else:
        print('编号不在[0,36]')
        
if __name__ == '__main__':
    num = input('请输入轮盘赌的pocket编号(0-36)==>')
    pocket_num()
