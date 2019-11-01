def bet(a):
    if a not in range(37):
        print('编号不在[0,36]')

    else:
        if a is 0:
            print('编号0的pocket颜色为绿色')      
            
        elif a%2 == 0:
            if number in (range(1,11) or range(19,29)):
                print('编号%s的pocket颜色为黑色'%(a))
            else:
                print('编号%s的pocket颜色为红色'%(a))

        else:
            if number in (range(1,11) or range(19,29)):
                print('编号%s的pocket颜色为红色'%(a))
            else:
                print('编号%s的pocket颜色为黑色'%(a))

if __name__ == '__main__':
    number = int(input ('请输入轮盘赌的pocket编号(0-36)==>'))
    bet(number)
    
            
