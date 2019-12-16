
import random

def guessnum():

    Goon = 'Y'
    while Goon in 'Yy':

        x = random.randint(1,100)
        ##print(x)##调试用
        gotit = False
        k = 1

        while not gotit and k<=4:

            numstr = input('[%d]:您猜的数是? '%k)

            try:
                
                num = int(numstr)

                if not 1<=num<=100:
                    print('请输入一个[1,100]范围的整数')
                    continue

            
                if x == num:
                    print('您猜对了!')
                    gotit = True
                elif num > x:
                    print('您猜的数太大了!')
                    k +=1
                elif num < x:
                    print('您猜的数太小了!')
                    k +=1

            except ValueError as e:
                print('{} {}'.format('请输入一个[1,100]范围的整数', e) )


            if k == 5:
                print('您已经猜了4次，要猜的数是%d'%x)
                
  

        Goon = input('继续游戏(Y/N)?...')
        print()


if __name__=='__main__':
    guessnum()
        
