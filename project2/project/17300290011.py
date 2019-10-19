def curren_time(wday,hour,minute):
    week = ['一','二','三','四','五','六','日']
    print('今天是星期%s,当前时间%02d：%02d' %(week[wday-1],hour,minute))


def interval_time(wday,hour,minute):
    week = ['一','二','三','四','五','六','日']
    interval = int(input('请输入一个时间间隔（分钟）'))
    today_minute = int(hour*60 + minute)
    interval_day = (interval+today_minute)//1440
    new_wday = (wday+ interval_day)%7
    print('在%d分钟之后是今天之后的%d天，那一天是星期%s' %(interval,interval_day,week[new_wday-1]))
    
def main():
    from project2_util import get_time
    wday,hour,minute = get_time()
    curren_time(wday,hour,minute)
    interval_time(wday,hour,minute)
    print('-'*40)

    from project2_util import test_datetime  
    test_datetime()


if __name__ == '__main__':
    main()
