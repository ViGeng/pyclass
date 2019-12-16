def main():
    quit = True
    while quit: 
        import random
        x=random.randint(1,100)
        i=1
        while i <5:
            try:
                print('[%d]:您猜的数是？'%i,end=' ')
                y=int(input())
            except ValueError as e:
                print ('请输入一个[1,100]范围的整数',e)
            else:
                if y<1 or y>100:
                    print ('请输入一个[1,100]范围的整数')
                else:
                    if x>y:
                        print ('您猜的数太小了！')
                        i+=1
                    elif x<y:
                        print ('您猜的数太大了！')
                        i+=1
                    else:
                        print ('您猜对了！')
                        break
        if i == 5:
            print('您已经猜了4次，要猜的数是%d'%x)
        z=input('继续游戏（Y/N）？...')
        if z != 'Y' and z!= 'y':
            quit = False
            

if __name__=='__main__':
    main()
