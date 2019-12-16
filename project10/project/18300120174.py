import random
num = random.randint(1,100)
def guess():
    global num
    i = 1
    while i <= 4:
        try:
            oppo = input("%d：您猜的数是？" % i)
            oppo = int(oppo)
        except Exception as r:
            print("请输入一个[1,100]范围的整数",r)
        else:
            global con
            con = 0
            if oppo > 0 and oppo < 101:
                i = i+1
                if oppo > num:
                    print("您猜的数太大了！")
                if oppo < num:
                    print("您猜的数太小了！")
                if oppo == num:
                    print("您猜对了！")
                    break
            elif oppo <= 0 or oppo >= 101:
                print("请输入一个[1,100]范围的整数")
            if i == 5:
                print("您已经猜了4次，要猜的数是%d" % num)
                num = random.randint(1,100)
                con = input("继续游戏(Y/N)?...")
guess()

if con == "Y" or con == "y":
    guess()
