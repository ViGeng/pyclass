import random
Set_number = random.randint(0,100)
N = 1
try:            
    Guess_number = int(input("[1]:您猜的数是?"))
except NameError and ValueError:
    print("请输入一个[1,100]范围的整数 invalid literal for int() with base 10:")
while N < 4:
    Guess_number = int(input("[%d]:您猜的数是?"%(N+1)))
    if  Guess_number == Set_number:
        break
    elif Guess_number > Set_number:
        print("您猜的数太大了")
    else:
        print("您猜的数太小了")
    N = N+1
if N < 4:
   print("您猜中了")
else:
   print('您已经猜了4次，要猜的数是%d'%(Set_number))
n=input('继续游戏（Y/N）？')
if n =='y'or'Y':
   print('[1]:您猜的数是?')
if n =='n'or'N':
   quit()     

                
                    
                 
                        
