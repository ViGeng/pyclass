
import math
import random

def game():
    flag=random.randint(1,100)
    
    i=0
    j=0
    while(i<4):
        i=i+1
        a=input("您猜的数是？")
        try:
            a=float(a)
            if a>=1 and a<=100:
                if a<flag:
                    print("您猜的数太小了！")
                elif a>flag:
                    print("您猜的数太大了！")
                else:
                    print("您猜对了！")
                    i=4
                    j=1
            else:
                print("请输入一个[1,100]范围的整数")
        except:
            print("请输入一个[1,100]范围的整数 invalid literal for int() with base 10:'%s'"%a)
        if i==4:
            if j==0:
                print("您已经猜了4次了，要猜的数是%d"%flag)
            j=0
            YN=input("继续游戏(Y/N)?...")
            if YN=="y":
                i=0
                flag=random.randint(1,100)
            elif YN=="n":
                break
            

if __name__=='__main__':
    game()

        

        


            
        
            
