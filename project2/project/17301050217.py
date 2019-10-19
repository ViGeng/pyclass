def get_time():
    import time
    current = time.localtime()
    now = list(current)
    return [now[3], now[4], now[6]+1]


def wday(wday):
    str_wday = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
    return str_wday[wday-1]


def main():
    now_num = get_time()[2] 
    print('今天是%s' % wday(now_num),end=',')
    print('当前时间','%02d:%02d' % (get_time()[0],get_time()[1]))
    #确定当前时间
    interval = int(input('请输入一个时间间隔(分钟)'))
    all_min = interval + get_time()[0]*60 + get_time()[1]
    then_day = all_min//(60*24)
    #确定之后天数
    wday_num = now_num + then_day 
    if wday_num <=7:
        then_wday = wday(wday_num)
    else:
        remainder = wday_num % 7
        then_wday = wday(remainder)
    #确定之后星期
    print('在%d分钟之后是今天之后的第%d天' % (interval,then_day),end=',')
    print('那一天是%s' % then_wday)

if __name__ == '__main__':     
    main()
