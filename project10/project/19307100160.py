def guessgame():
    answer = random.randint(1,100)
    count = 1
    while True:
        try:
            number = int(input('[%s]:您猜的数是'%(count)))
            if 1 <= number <=100:
                if number < answer:
                    print('您猜的数太小了！')
                    count += 1
                    if count >= 5:
                        print('您已经猜了4次，要猜的数是%d'%(answer))
                        break
                    continue
                if number > answer:
                    print('您猜的数太大了！')
                    count += 1
                    if count >= 5:
                        print('您已经猜了4次，要猜的数是%d'%(answer))
                        break
                    continue
                if number == answer:
                    print('您猜对了')
            else:
                count += 1
                print('请输入一个[1,100]范围的整数')
                continue
            break
        except ValueError as e:
            print("请输入一个[1,100]范围的整数 invalid literal for int() with base 10:'%s'"%(e))           
            count += 1
            continue
    x = input('继续游戏(Y/N)？...')
    if x == 'Y':
        guessgame()
    if x == 'N':
        print('游戏结束')


if __name__ == '__main__':
    import random
    guessgame()       
