
import random

def guess_number():
    play = True
    while play:
        a = random.randint(1,100)
        n = 1
        while n <= 4:
             try:
                 num = input('[%d]:您猜的数是？'%n)
                 numg = int(num)
             except ValueError as e:
                 print('请输入一个[1,100]范围内的整数',e)
                 continue
             if numg < 0 or numg > 100:
                 print('请输入一个[1,100]范围内的整数')
                 continue
             else:
                  n+=1
                  if numg == a:
                      print('您猜对了！')
                      break
                  else:
                       if numg < a:
                           print('您猜的数太小了！')
                       elif numg > a:
                           print('您猜的数太大了！')
                        
        else:
             print('您已经猜了4次，要猜的数是%d'%a)
                               
        y_n = str(input('继续游戏(Y/N)?'))
        if  y_n != 'Y'and y_n != 'y':
             play = False

                 
    return num            
               

if __name__ == '__main__':
    guess_number()
    
