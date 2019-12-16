# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def guess_game():
    import random 
    my_number = random.randint(1,101)
    found = False
    while not found:
        n = 1
        while n < 5:
            u_number = input('[%d]您猜的数是？'%(n))
##            if u_number == '':
##                print('请输入一个[1,100]范围的整数 invalid literal for int() with base 10:%s'%(''))
            try:
                u_number_1 = int(u_number)
                if 0<= u_number_1 <= 100:
                    if u_number_1 < my_number:
                        print('您猜的太小了！')
                    elif u_number_1 > my_number:
                        print('您猜的太大了！')
                    elif u_number_1 == my_number:
                        print('您猜对了！')
                        if_c = input('继续游戏(Y/N)?...')
                        if if_c == 'y' or if_c =='Y':
                            found = True
                            break
                        else:
                            found = False
                            break
                        break
                else:
                    print('请输入一个[1,100]范围的整数') 
            except ValueError as e:
                print('请输入一个[1,100]范围的整数 invalid literal for int() with base 10:%s'%(e))
            n += 1
        print('您已经猜了%d次，要猜的数是%d'%(n-1,my_number))
        if_c = input('继续游戏(Y/N)?...')
        if if_c == 'y' or if_c =='Y':
            found = False      
        else:
            found = True
            break
        

        
                
if __name__ == '__main__':
    guess_game()
            
            
                
