from project2_util import get_time:                                                              n
def in_pu():
    minutes = print ("请输入一个时间间隔（分钟）：")
    return minutes

def compute(wday,hour,x):

    a=int(hour)*60 + int(minute) + int (x)
    if a <= 1440:
        print("在" + str(x) + "分钟之后是今天之后的第0天，"+"那一天是"+str(wday))
    elif a>1440 and a<=10000:
        b = int((a-1440)/1440)
        c = b-(7-int(waday))
        print("在" + str(x) + "分钟之后是今天之后的第"+b+"天，"+"那一天是"+str(wday))
    else:
        b = int((a-1440)/1440)
        c = (a-1440)%10000
        d = int(int(c)/1440)
        f = b-(7-int(waday))
        print("在" + str(x) + "分钟之后是今天之后的第"+b+"天，"+"那一天是"+str(f))

def main():
    wday,hour,minute=get_time()
    print("今天是"+wday+","+"当前时间"+hour+minute)
    minutes = in_pu()
    compute(wday,hour,minute)

f__name__=='main':
    main()
    
