import random
import sys

def main():
    again = 'Y'
    while again == 'y' or again == 'Y':
        a = random.randint(1,100)
        t = 1
        while t < 5:
            try:
                x = input('[%d]您猜的数是？' %(t))
                y = int(x)
            except ValueError as inst:
                print('%s%s' %('请输入一个[1,100]范围内的数 ', inst))
            else:
                if y == a:
                    print('您猜对了！')
                    t += 1
                    break
                elif 1 <= y < a:
                    print('您猜的太小了！')
                    t += 1
                elif a < y <= 100:
                    print('您猜的太大了！')        
                    t += 1
                elif y < 1 or y > 100:
                    print('请输入一个[1,100]范围内的数')
        if t == 5:
            print('%s%d' %('您已经猜了4次，要猜的数是', a))
            again = str(input('继续游戏(Y/N)?'))
    else:
        sys.exit()

if __name__ == '__main__':
    main()
