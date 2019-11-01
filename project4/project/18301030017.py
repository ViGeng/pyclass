x=int(input('请输入轮盘赌的pocket编号(0-36)==>'))
def func():
    
    if x>36:
        return'编号不在[0-36]'
    elif x>=1 and x<=10 or (x>=19 and x<=28) and x%2==0:
        print('编号%d的pocket颜色为黑色'%x)
    elif x>=1 and x<=10 or (x>=19 and x<=28) and x%2==1:
        print('编号%d的pocket颜色为红色'%x)
    elif x>=11 and x<=18 or (x>=29 and x<=36) and x%2==0:
        print('编号%d的pocket颜色为红色'%x)
    elif x>=11 and x<=18 or (x>=29 and x<=36) and x%2==1:
        print('编号%d的pocket颜色为黑色'%x)

func()
    
