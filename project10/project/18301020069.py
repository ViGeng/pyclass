import random
def guess_bot():
    i = 1
    SuiJiShu = int(random.randint(1, 100))
    while i <= 4:
        i += 1
        GuessNum = int(input('请输入猜测： '))
        if GuessNum == SuiJiShu:
            print('恭喜！！猜测正确')
            print('系统生成随机数为%d' %SuiJiShu)
            exit()
        elif GuessNum > SuiJiShu:
            print('您输入的数太大了！')
        else:
            print('您输入的数太小了！')
    print('系统生成随机数为%d' %SuiJiShu)

def re():
    for times in range(1, 6):#不会取到右边的数，别忘了
        print("#####您已累计玩了本游戏共", times-1 ,"次#####")
        if times == 1:
            print("#####这是您第 1 次玩猜数字游戏#####")
            guess_bot()
             
        elif times == 5:
            print("#####您最多能玩4次#####")
            print("#####请注意休息#####")
            break
         
        else:
            if_again = input("是否再来一次?(Y/N):")
            if if_again == "Y":
                guess_bot()
            elif if_again == "N":
                print("欢迎您的下次启用")
                break
            else:
                print("虽然不明白您什么意思 小的还是关了吧")
                break
             
try:
    re()
except ValueError:
    print("部分值不能为空")
except UnboundLocalError:
    print("引起该错误可能是由于某个值为空,不能进行比较")
finally:
    print("程序退出")
 
