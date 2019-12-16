import random

def guesswhat():
    correctnumber = random.randint(1,100)
    i=1
    guessnumber = input('[%s]:您猜的数是？'%(i))
    while guessnumber:
        if i in [1,2,3,4]:
            try:
                guessnumber = int(guessnumber)
                if 1<=guessnumber<=100:
                    i+=1
                    if guessnumber == correctnumber:
                        i=0
                    if guessnumber < correctnumber:
                        print('您猜的数太小了！')
                    if guessnumber > correctnumber:
                        print('您猜的数太大了！')
                else:
                    print('请输入一个[1,100]范围的整数')
            except ValueError as e:
                print('请输入一个[1,100]范围的整数 ',e)
            if i in [1,2,3,4]:
                guessnumber = input('[%s]:您猜的数是？'%(i))
            else:
                break           
        else:
            break

            
    if i == 0:
        print('您猜对了！')
    else:
        print('您已经猜了4次，要猜的数是%s'%(correctnumber))


    a = input('继续游戏（Y/N）?')
    if a in ['y','Y']:
        guesswhat()


if __name__ == '__main__':
    guesswhat()
          
            

