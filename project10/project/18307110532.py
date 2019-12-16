import random
x=random.randint(1,100)
def input_number(i):
    while True:
        try:
            print("[",i,"]:",sep='',end='')
            a=int(input("您猜的数是？"))
            if (a<=0 or a>100):
                print("请输入一个[1,100]范围的整数")
            else:
                break
            
        except ValueError as e:
            print("请输入一个[1,100]范围的整数",'{}'.format(e))
                
    return a

while True:
    #一次游戏
    #询问是否再玩，不玩就break
    j=1
    i=1
    z=0
    y=101
    while i < 5:
        a=input_number(i)
        if z<a<y:
            if a>x:
                print("您猜的数太大了！")
                y=a
            if a<x:
                print("您猜的数太小了！")
                z=a
            if a==x:
                print("您猜对了！")
                j = 0
                break
            i=i+1
        else:
            if a<z:
                print('比上个偏小的数还小，请重试：')
            if a>y:
                print('比上个偏大的数还大，请重试：')
        
    if(j == 1):
        print("您已经猜了4次，要猜的数是",x)
    c=input("继续游戏(Y/N)?...")
    if c ==( 'n' or 'N'):
        break
    
    
