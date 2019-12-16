import random
def input_int(k=1):
    while True:
        try: 
            guessnumber = int(input('[%d]:您猜的数是?' % k))
            if 1 <= guessnumber <= 100:
                break
            else:
                print('请输入一个[1,100]范围的整数')
        except ValueError as ve:
            print('请输入一个[1,100]范围的整数 invalid literal for int() with base 10:{}'.format(ve))
    return guessnumber


def guess_reminder(realnumber, guessnumber):
    k = 1
    while k < 4:
        if realnumber == guessnumber:
            print('您猜对了')
            next_game()
            break
        elif realnumber < guessnumber:
            print('您猜的数太大了')
            k += 1
        else:
            print('您猜的数太小了')
            k += 1
        input_int(k)
    else:
        print('你已经猜了4次，要猜的数是%d' % realnumber)
        next_game()

            
def next_game():
    while True:
        target = input('继续游戏(Y/N)?...')
        if target is 'Y' or target is 'y':
           realnumber = random.randint(1,100)
           print(realnumber)
           guessnumber = input_int(k=1)
           guess_reminder(realnumber,guessnumber)
        else:
            break  
    
    
if __name__ == '__main__':
    realnumber = random.randint(1,100)
    print(realnumber)
    guessnumber = input_int(k=1)
    guess_reminder(realnumber,guessnumber)
