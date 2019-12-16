import random

def main():
    result = random.randint(1,100)
    guess_chances = 4
    for i in range(1,guess_chances+1):
        guess = input('您猜的数是？')
        if guess.isdigit():
            guess = int(guess)
            if guess < result:
                print('您猜的数太小了!')
            elif guess > result :
                print('您猜的数太大了!')
            elif guess == result :
                print('您猜对了！')
                break
        else:
            print ('请输入一个[1,100]范围的整数 invalid literal for int() with base 10:‘', guess ,'’')

    while (guess_chances - i) == 0 :
        print ('您已经猜了4次，要猜的数是' ,result)
        break
    
    answer = input('继续游戏(Y/N)?')
    if answer == 'Y':
        main()


if __name__ == '__main__':
    main()

    
