import random
num = random.randint (1,100)
print (num)     # 用来检查后面程序的运行是否准确

for guesstake in range (1,5):
    print ('[%d]:您猜的数是？' % guesstake)
    try:
        guess = int (input())
    except ValueError:
        print ('请输入一个[1-100]范围的整数 invalid literal for int() with base 10:')
        continue

    if guess == num:
        print ('您猜对了！')
        break
    elif guess < 0 or guess > 100:
        print ('请输入一个[1-100]范围的整数')
    elif guess < num:
        print ('您猜的数太小了！')
    elif guess > num:
        print ('您猜的数太大了！')
    
     
if guesstake == 4:
    answer = input('您已经猜了4次，要猜的数是%d''\n继续游戏(Y/N)?...' % num)
    if answer.lower() == 'y':
        guesstake += 1
              
    else:
        answer.lower == 'n'
        print ('游戏结束')
        
        
        
        
        
       
        
    
       
        
        
           
