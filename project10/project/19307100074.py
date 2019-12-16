def guessnumber():
    import random
    answer = random.randint(0,100)
    a = 0
    while (4-a):
        number = input('您猜的数是？')
        try:
            true= int(number)
            if true>100 or true<0:
                print('请输入一个[1,100]范围的整数')
            else:
                a +=1
                if true== answer:
                    print('[',a,']','您猜对了！')
                    break
                elif true>answer:
                    print('[',a,']','您猜的数太大了！')
                else:
                    print('[',a,']','您猜的数太小了！')
        except ( TypeError, ValueError)as mistake:
            print('请输入一个[1,100]范围的整数',type(mistake),mistake)
        except:
            raise
        if a ==4:
            print('您已经猜了四次，要猜的数是',answer)

b= 1
while b:
    guessnumber()
    choice =input('继续游戏？（Y/N）')
    if choice is 'Y' or choice is 'y':
        b=1
    else:
        b+=-1
        
        
                
