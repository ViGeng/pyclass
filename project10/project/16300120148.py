import random
while True:
    num = random.randint(1, 100)
    end = False
    index = 1
    while True:
        guess = input('[%d]:您猜的数是？' %index)
        try:
            num_guess = int(guess)
        except ValueError as e:
            print('请输入一个[1,100]范围的整数 ', e)
            continue

        if 1 <= num_guess <= 100:
            if num_guess > num:
                print('您猜的数太大了！')
            elif num_guess < num:
                print('您猜的数太小了！')
            else:
                print('您猜对了！')
                end = True
                break
            if index == 4:
                print('您已经猜了4次，要猜的数是', num)
                end = True
                break
            index += 1
        else:
            print('请输入一个[1,100]范围的整数 ')

    if end:
        choice = input('继续游戏(Y/N)?...')
        if choice == 'y' or choice == 'Y':
            pass
        else:
            break
