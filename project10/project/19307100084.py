import random
def input_int():
    prizenumber=random.randint(1,100)
    s = 1
    while s <= 4:
        print('[',s,']',':您猜的数是？')
        x = input("\n") 
        s = s+1
        try:
            x=int(x)
            if x == prizenumber:
                print('您猜对了！\n')
                break
            elif x<=0:
                print('请输入一个[1,100]范围的整数')
            elif x>=prizenumber:
                print('您猜的数太大了！')
            elif x<=prizenumber:
                print('您猜的数太小了！')
        except ValueError as e:
            print('请输入一个[1,100]的整数 invalid literal for int()' ) 
    print('您已经猜了',s-1,'次，要猜的数是',prizenumber,'\n')
    print('继续游戏（Y/N）？...')
    choice=input("\n")
    if choice==('Y') or choice == ('y'):
        input_int()
input_int()
