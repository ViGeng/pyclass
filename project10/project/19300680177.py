def main():
    quit = True
    while quit: 
        import random
        x = random.randint(1,100)
        i = 1
        while i <= 4:
            try:
                print('[%d]:您猜的数是？'%i, end=' ')
                y = int(input())
            except ValueError as t:
                print ('请输入一个[1,100]范围的整数', t)
            else:
                if y<1 or y>100:
                    print ('请输入一个[1,100]范围的整数')
                else:
                    if x > y:
                        print ('您猜的数太小了！')
                        i += 1
                    elif x < y:
                        print ('您猜的数太大了！')
                        i += 1
                    else:
                        print ('您猜对了！')
                        break
        if i == 5:
            print('您已经猜了4次，要猜的数是%d'%x)
            print('继续游戏（Y/N）？...', end=' ')
        z = input()
        if z != 'Y' and z != 'y':
            break
            

if __name__=='__main__':
    main()
