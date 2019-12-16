import random

def input_int(i):
    x=0
    while True:
        try:
            while x<=0 or x>=101:
                 x=int(input("[%d]:您猜的数是？"%i))
                 if x <= 0 or x>=101:
                    print('请输入一个[1,100]范围的整数')
            break
        except Exception as e:
            print('请输入一个[1,100]范围的整数'+" "+str(e))
            
    return x

while True:
    a=random.randint(1,100)
    for i in range(1,5):
        b=input_int(i)
        if a>b:
            print('您猜的数太小了！')
        if a<b:
            print('您猜的数太大了！')
        if a==b:
            print("您猜对了!")
            break
    if a!=b:
        print('您已经猜了4次，要猜的数是%d'%a)
    c=str(input("继续游戏(Y/N)?..."))
    if c!='y' and 'Y':
        break
