def guess_number():
    import random
    n = random.randint(1,100)
    i = 1
    while i <=4:
        try:
            a = int(input("[%d]:您猜的数是？"%i))
            if a == n:
                print("您猜对了!")
                break
            elif a < n and a >=1:
                print("您猜的数太小了!")
                i += 1
            elif a > n and a <=100:
                print("您猜的数太大了!")
                i += 1
            else:
                print("请输入一个[1,100]范围的整数")
        except ValueError as k:
            print("请输入一个[1,100]范围的整数",k)
        if i == 5:
            print("您已经猜了4次，要猜的数是%d"%n)    
   
        
if __name__ == '__main__':
     while True:
        guess_number()
        while True:
            b = input("继续游戏(Y/N)?...")
            if b in ['y','Y','n','N']:
                break
            else:
                print("请输入Y/y/N/n")
        if b =='n' or b == 'N':
            break
    
