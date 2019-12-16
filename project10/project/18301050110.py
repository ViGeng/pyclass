import random

def play_game():
    a = random.randint(1,100)
    n = 1
    while True:
        try:
            b = int(input('[%d]:您猜的数是？'%(n)))
            if b < 1 or b >100:
                print('请输入一个[1,100]范围的整数')
            if a != b :
                if b > a:
                    print('您猜的数太大')
                    n += 1
                if b < a:
                    print('您猜的数太小了！')
                    n += 1
                if n > 4:
                    print('您已经猜了4次，要猜的数是%d'%(a))
                    break
            if a == b:
                print('您猜对了!')
                break
        except ValueError as e:
            print('请输入一个[1,100]范围的整数 invalid literal for int() with base 10:',e) 
    return


play_game()
d = 1
while d == 1:
    c = input('继续游戏（Y/N）?...')
    if c == 'y'or c == 'Y':
        play_game()
    else:
        break
    pass
        
        
    
    
    
