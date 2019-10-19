 # -*- coding: UTF-8 -*-

""" 显示当前时间，并询问用户一个时间间隔后汇报间隔后过了几天是星期几
""" 


import project2_util


def report_time():
    string='一二三四五六天'
    #print(string[6])
    wday,hour,minute=project2_util.get_time()
    #print(wday)
    print('今天是星期' + string[wday-1] + ',当前时间%02d:%02d' % (hour,minute))
    interval = int(input('请输入一个时间间隔（分钟）'))
    today_minute = hour * 60 + minute
    future_minute = today_minute + interval
    interval_day = future_minute // 1440
    now_wday = (wday + interval_day) % 7
    #print(now_wday)
    print('在%d分钟之后是今天之后的第%d天,那一天是星期' % (interval,interval_day) + string[now_wday-1])


if __name__ == '__main__':
    report_time()
