import random
continue_=True
while continue_:
    i=1
    number=random.choice(range(1,101))
    while i<=4:
        try:
            guess=int(input('您猜的数是？'))
            if guess>number:
                print('您猜的数太大了!')
            if guess<number:
                print('您猜的数太小了!')
            if guess==number:
                print('您猜对了!')
                break
            i+=1
        except ValueError as e:
             print('请输入一个[1,100]范围的整数',e)
    else:
        print('您已经猜了4次,要猜的数是%d' % (number))
    ask=str(input('继续游戏(Y/N)?'))
    if ask=='y' or ask=='Y':
        continue_=False
    
        
    
