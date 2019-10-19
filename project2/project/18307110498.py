def get_times():
    """ 返回有关当前时间的3个信息组成的元组，分别为wday, hour, minute
    wday表示本周的星期几，取值范围[1,7]，其中7表示星期天
    hour取值范围[0,23]，分钟取值范围[0,59]，表示当前时间的小时和分钟数
    """ 
    import time
    current =time.localtime()
    return current.tm_wday + 1 , current.tm_hour, current.tm_min

def str_wday(wday):
    wdays = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
    return wdays[wday-1]

if __name__ == '__main__':
    print()
    wday,hour,minute = get_times()

    print('今天是%s，当前时间%d:%d' % (str_wday(wday), hour, minute))
    interval = int(input('请输入一个时间间隔（分钟）'))
    interval_ = interval + hour * 60 + minute
    days = int(interval_ // (24 * 60))
    wday_ = (wday + days) % 7

    print('在%s分钟后是今天之后的第%d天，那一天是%s。' % (interval, days, str_wday(wday_))) 
    
