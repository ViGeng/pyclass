def main():
    n = int(input('请输入轮盘赌的pocket编号(0-36)==>'))
    if n==0:
        a='绿色'
        print('编号%d的pocket颜色为'%n+a) 
    elif  n in range (1,11) or n in range (19,29):
        if n%2==0:
            a='黑色'
        else :
            a='红色'
        print('编号%d的pocket颜色为'%n+a) 
    elif  n in range (11,19) or n in range (29,37):
        if n%2==0:
            a='红色'
        else :
            a='黑色'
        print('编号%d的pocket颜色为'%n+a)    
    else:
        print('编号不在[0,36]')
    

if __name__ == '__main__':
    main()
