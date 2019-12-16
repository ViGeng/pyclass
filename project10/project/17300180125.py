import random
def get_key():
    """返回一个标准答案，范围在1到100之间
    """
    return random.randint(1,100)

def judge(key):

    """游戏主体
    """
    i=1
    while 0< i <5:
        answer=int(input(str([i])+'您猜的数是？'))
        if answer==key:
            print("您猜对了！")
            break
        elif 1 <= answer < key :
            print("您猜的数太小了！")
            if i==4:
                print("您已经猜了4次，要猜的数是",key)
        elif 100 >= answer > key :
            print("您猜的数太大了！")
            if i==4:
                print("您已经猜了4次，要猜的数是",key)
        else:
            print("请输入一个[1,100]范围内的整数")
        i+=1
            
            
if __name__=='__main__':
    k=1
    """循环的设置是为了重复进行游戏
    """
    while k >= 1 :
        try:
            key=get_key()
            judge(key)
            a=input("继续游戏（Y/N）？")
            if a=='y' or a=='Y':
                k+=1
                continue
            else:
                break
        
        except ValueError as e:
             print('请输入一个[1,100]范围内的整数',e)
