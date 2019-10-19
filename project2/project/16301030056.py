
def str_wday():
    import time
    current = time.localtime()
    week_day_dict = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
    wday = week_day_dict[current.tm_wday]
    print('今天是%s,当前时间%02d:%02d' % (wday,current.tm_hour,current.tm_min)) 
    interval = int(input('请输入一个时间间隔（分钟）'))
    t = int(interval//(60*24))
    wday_after = week_day_dict[(current.tm_wday + t)%7]
    print('在%s分钟之后是今天之后的第%d天,那一天是%s' % (interval,t,wday_after))
    


if __name__ == '__main__':    

    str_wday()
