import random
while True:
    n = random.randint(1,100)
    i = 1
    while True:
        try:
            print('[%d]'%i,end='')
            m = int(input('您猜的数是？'))
        except ValueError as e:
            print('请输入一个[1,100]范围的整数 {}'.format(e))
        else:
            if m < 0 or m > 100:
                print('请输入一个[1,100]范围的整数')
                while True:
                    try:
                        print('[%d]'%i,end='')
                        m = int(input('您猜的数是？'))
                    except ValueError as e:
                        print('请输入一个[1,100]范围的整数 {}'.format(e))
                    else:
                        if m == n:
                            print('您猜对了')
                            i = 4
                        elif m > n:
                            print('您猜的数太大了')
                        else:
                            print('您猜的数太小了')
                        i += 1
                    finally:
                        if i > 4:
                            break
            else:
                if m == n:
                    print('您猜对了')
                    i = 4
                elif m > n:
                    print('您猜的数太大了')
                else:
                    print('您猜的数太小了')
                i += 1
        finally:
            if i > 4:
                break
    if m != n:
        print('您已经猜了4次，要猜的数是%d'%n)
    a = str(input('继续游戏(Y/N)?...')).lower()
    if a != 'y':
        break
