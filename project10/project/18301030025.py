import random
def judge(number):
    while not number.isdigit():
        print("请输入一个[1，100]范围的整数 invalid literal for int() with 10:'%s'" % number)
        number = input("您猜的数是？")
    num = int(number)
    if (num<0) or (num>100):
        print("请输入一个[1，100]范围的整数")
        number = input("您猜的数是？")
        judge(number)
    return num
T = "Y"
while T == "Y" or T == "y":
    num = random.randint(1,100)
    for i in range(0,5):
        if i != 4:
            count = str(6-i)
            number = input("您猜的数是？")
            number = judge(number)
            if number == num:
                print("您猜对了")
                break
            else:
                if number > num:
                    print("您猜的数太大了！")
                else:
                    print("您猜的数太小了！")
        else:
            print ("您已经猜了4次，要猜的数字是:",num)
            break
    T = input("继续猜数字游戏请输入y/Y，输入其它任意键退出：")
