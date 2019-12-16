
guess = 0
tries = 1
answer = 'Y'
print('请输入[1,100]之间的整数，你只有四次猜测机会')

while answer == 'Y':
    import random
    number = random.randint(1,100)
    while guess != number and tries < 5:
        x = input('[%d]:您猜的数是？'% tries)

        try:
            guess = int(x)
        except ValueError:
            print("请输入一个[1,100]范围的整数 invalid literal for int() with base 10:"+ x)
            continue

        if guess<1 or guess>100:
            print('请输入一个[1,100]范围的整数')
            continue

        if guess < number:
            print('您猜的数字太小了！')
        elif guess > number:
            print('您猜的数字太大了！')
        tries = tries + 1

    if guess == number:
         print('您猜对了！')

    else:
        print('您已经猜了4次，要猜的数是',number)
    tries = 1
    answer = input('是否要继续？(Y/N)')
            


    

        

