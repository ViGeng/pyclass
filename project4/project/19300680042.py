if __name__ == '__main__':
    number = int(input('请输入轮盘赌的pocket编号（0-36）==>'))
    if number == 0:
        print ('编号',number,'的pocket颜色为绿色')
    elif number <= 10:
        if number%2 ==0:
            print ('编号',number,'的pocket颜色为黑色')
        else :
            print ('编号',number,'的pocket颜色为红色')
    elif number <= 18:
        if number%2 ==0:
            print ('编号',number,'的pocket颜色为红色')
        else :
            print ('编号',number,'的pocket颜色为黑色')
    elif number <= 28:
        if number%2 ==0:
            print ('编号',number,'的pocket颜色为黑色')
        else :
            print ('编号',number,'的pocket颜色为红色')
    elif number <= 36:
        if number%2 ==0:
            print ('编号',number,'的pocket颜色为红色')
        else :
            print ('编号',number,'的pocket颜色为黑色')
    else:
        print ('编号不在[0,36]')
