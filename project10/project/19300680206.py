import random
wrong = '请输入一个[1，100]范围的整数'

def guess_number():
    i = 1
    x = random.randint(1, 100)
    while i <= 5:
        if i == 5:
            print('您已经猜了4次，要猜的数是%d' % x)
            s = input('继续游戏(Y/N)？')
            if s == 'Y' or s == 'y':
                i = 1
                x = random.randint(1, 100)
            else:
                break
        else:
            try:
                t = int(input('[%d]:您猜的数是？' % i))
                if t == x:
                    print('您猜对了！')
                    break
                elif t < 1 or t > 100:
                    print(wrong)
                elif t < x:
                    print('您猜的数太小了！')
                    i += 1
                elif t > x:
                    print('您猜的数太大了！')
                    i +=1
            except ValueError as e:
                print(wrong, e)

if __name__ == "__main__":
    guess_number()
