import random
def guess_number():
    n = random.randint(1,100)
    count = 1
    while True:
        try:
            x = int(input('[%d]您猜的数是？'%(count)))
            if x < 1 or x > 100:
                print('请输入一个[1,100]范围的整数')
                continue
            if x == n:
                print('您猜对了！')
                st = input('继续游戏(Y/N)?...')
                if st == 'Y' or st == 'y':
                    n = random.randint(1,100)
                    count = 1
                    continue
                else:
                    break
            elif x > n:
                print('您猜的数太大了！')
                count += 1
            else:
                print('您猜的数太小了！')
                count += 1
            if count > 4:
                print('您已经猜了4次，要猜的数是%d'%(n))
                s = input('继续游戏(Y/N)?...')
                if s == 'Y' or s == 'y':
                    n = random.randint(1,100)
                    count = 1
                    continue
                else:
                    break
        except Exception as e:
            print('请输入一个[1,100]范围的整数',e)

if __name__ == '__main__':
    guess_number()
