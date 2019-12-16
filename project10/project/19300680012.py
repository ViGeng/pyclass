import random

def guess_number():
    number = random.randint(1,100)
    i = 1
    while i <= 4:
        try:
            guess = int(input("[%d]: 您猜的数是?"%(i)))
            if 1 <= guess <= 100:
                if guess == number:
                    print("您猜对了")
                    break
                elif guess < number:
                    print("您猜的数太小了!")
                    i=i+1
                elif guess > number:
                    print("您猜的数太大了!")
                    i=i+1
            else:
                print("请输入一个[1,100]范围的整数")
        except ValueError as e:
            print("请输入一个[1,100]范围的整数 %s"%e)

    print("您已经猜了4次，要猜的数是%d"%number)

def main():

    while True:
        guess_number()
        if input("继续游戏(Y/N)?...").upper() == "N":
            break

if __name__ == "__main__":
    main()
