#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def get_time():
    """ 返回有关当前时间的3个信息组成的元组，分别为wday, hour, minute
    wday表示本周的星期几，取值范围[1,7]，其中7表示星期天
    hour取值范围[0,23]，分钟取值范围[0,59]，表示当前时间的小时和分钟数
    """
    import time
    current = time.localtime()
    return current.tm_wday + 1, current.tm_hour, current.tm_min


def test_datetime():
    import datetime
    now = datetime.datetime.now()
    print('当前时刻：%d-%02d-%02d %02d:%02d' % (now.year, now.month, now.day, now.hour, now.minute))
    interval_now = now - datetime.datetime(year=now.year, month=1, day=1)
    # print(interval_now)
    print('今年的第%d天' % (interval_now.days + 1))

    if now.month == 12:
        next_month = now.replace(year=now.year + 1, month=1, day=1)
    else:
        next_month = now.replace(month=now.month + 1, day=1)
    print('还有%d天到下个月' % (next_month - now).days)

    interval = float(input('请输入一个时间间隔（分钟）'))
    t = now + datetime.timedelta(minutes=interval)
    print(t.strftime('未来时刻：%Y-%m-%d %H:%M'))
    print('过去了%d天' % (t.toordinal() - now.toordinal()))
    print('那一天是', t.strftime('%A'))


def str_wday(wday):
    """返回中文的星期几
    wday表示本周的星期几，取值范围[1,7]，其中7表示星期天

    """
    return wday


if __name__ == '__main__':
    #    wday,hour,minute = get_time()
    #    print(wday, hour, minute)
    test_datetime()

