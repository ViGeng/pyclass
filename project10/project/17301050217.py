
def guess_num(cishu = 4):
    import random
    fix_num = random.randint(1,100)
    count = 1
    while count<=cishu:
        try:
            x = int(input('[%d]:您猜的数是? ' % count))
            if x<1 or x>100:
                print('请输入一个[1,100]范围内的整数')
                continue
        except ValueError as e:
            print('请输入一个[1,100]范围内的整数',e) 
        else:
            count+=1
            if 0<=x<fix_num:
                print('您猜的数太小了!')
            if fix_num<x<=100:
                print("您猜的数太大了!")
            if x == fix_num:
               print('您猜对了!')
               break
                   
        finally:
            if count==5:
                print('您已经猜了4次,要猜的数是%d' % fix_num)
        
         
if __name__ == '__main__':
    guess_num(cishu=4)
