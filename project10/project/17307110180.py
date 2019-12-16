import random

numbers = list(range(1,101))
answer = random.choice(numbers)
#print(answer) 此处不打印答案


time = 1
while True:
    try:
        f_guess = (input('[{0:d}]:您猜的数是?'.format(time)))
        guess = int(f_guess)
    except ValueError as e:
        print("请输入一个[1,100]范围的整数 invalid literal for int() with base 10: '{}'".format(f_guess))
        continue
    if guess == answer:
        print("您猜对了！")
        break
    if guess <= 0 or guess > 100:
        print("请输入一个[1,100]范围的整数")
        continue
    if guess < answer:
        print("您猜的数太小了!")
        time += 1
    if guess > answer:
        print("您猜的数太大了！")
        time += 1
    if time == 5:
        print("您已经猜了4次，要猜的数是{}".format(answer))
        con_next = input("继续游戏(Y/N)?...")
        if con_next == 'Y' or con_next == 'y':
            time = 1
        else:
            print('game over')
            break
    
    
    
