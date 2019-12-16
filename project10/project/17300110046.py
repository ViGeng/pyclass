import random
a = random.randint(1,100)
c = 0

while c<4:
    b = input('您猜的数是？')
    if b.isdigit() and 0<int(b)<101:
        b = int(b)
        if b>a:
            print('您猜的数太大了！')

        elif b<a:
            print('您猜的数太小了！')
        elif b==a:
            print('恭喜您猜对了！')
            break
        c+=1
    else:
        print('请输入一个[1,100]范围内的整数')
    
    if c==4:
        print('您已经猜了4次，正确答案是%d'%a)
        t=input('继续游戏(Y/N)？...')
        if t=='Y':
            c = 0
            a = random.randint(1,100)
        elif t=='N':
            c+=1
