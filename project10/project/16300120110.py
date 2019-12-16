from random import randint

def main():
    flag=1
    maxValue = 100

    while flag :
        value = randint(0,maxValue)
        prompt = ("您猜的数是?")

        for i in range (1,5):
            
            while 1:
                try:
                    x=int(input(prompt))
                    if x < 0 or x > 100:
                        print("[%i]请输入一个[0，100]的整数"%(i))
                        continue
                    else:
                        break

                except Exception as e:
                    print("[%i]请输入一个[0，100]的整数"%(i),e)
                    continue

            if x > value:
                print("[%i]您猜的数太大了！"%(i))
            elif x < value:
                print("[%i]您猜的数太小了！"%(i))
            else:
                print("[%i]您猜对了！"%(i))
                break

            if i==4:
                print("您已经猜了4次，要猜的数是%i"%(value))

        if str(input("继续游戏(Y/N)?")) == "N" or "n":
            flag=0


if __name__ == '__main__':
    main()


