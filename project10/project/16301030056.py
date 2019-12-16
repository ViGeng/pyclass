import random
def kkk():
 random_num = random.randint(1,100)
 time = 1
 while time < 5:
        r = input('[%d]您猜的数是?'% time)
        if r.isdigit():
            num = int(r)
            if num == random_num:
                break;
            elif num < random_num:
               print ("您猜的数太小了")
            else:
               print ("您猜的数太大了.")
            time = time+1
        else:
            print('错误')
            r = input('[%d]您猜的数是?'% time)
            if r.isdigit():
                num = int(r)
                if num == random_num:
                    break;
                elif num < random_num:
                    print ("您猜的数太小了")
                else:
                    print ("您猜的数太大了.")
                time = time + 1
 if time < 5:
    print ("您猜对了！")
 else:
    print ("您已经猜了4次，要猜的数是%d" % random_num)
 return time       

def main():
    m = input('是否继续(y/n)')
    if m == 'y':
        kkk()
    else:
        print('结束')

if __name__ == '__main__':
    kkk()
    main()
    

