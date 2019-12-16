import random

def sum_guess():
    ran_number = int(random.randint(1,100))
    play = True
    while play:
        count = 1
        while count <= 4:
            try:
                guess_number = int(input("[%d]:您猜的数是？"%count))
                if guess_number <= 0 or guess_number>100:
                    print("请输入一个[1,100]范围的整数")
                elif guess_number > ran_number:
                    print("您猜的数太大了！")
                    count+=1
                elif guess_number < ran_number:
                    print("您猜的数太小了！")
                    count+=1
                else:
                    print("您猜对了！")
                    break
            except(NameError,ValueError) as inst:
                print("请输入一个[1,100]范围的整数 invalid literal for int() with base 10:",inst)
        else:
            print("您已经猜了%d次，要猜的数是%d"%((count-1),ran_number))
            
        player_choice = True
        while player_choice:
            choice = str(input("继续游戏(Y/N)?"))
            if choice != 'y' and choice != 'Y':
                play = False
            player_choice = None

if __name__ == '__main__':
    sum_guess()
            
