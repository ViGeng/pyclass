#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import project2_util

def convert_wday(x):
    weekday = ['星期一','星期二','星期三','星期四','星期五',
               '星期六','星期天']
    wday = weekday[int(x[0]) - 1]
    return wday

def convert_hour(x):
    hour = x[1]
    return hour

def convert_minute(x):
    minute = x[2]
    return minute

def convert_wday_2(x,y):
    weekday = ['星期一','星期二','星期三','星期四','星期五',
               '星期六','星期天']
    wday_2 = weekday[(int(x[0]) + y - 1) % 7]
    return wday_2

def main():
    x = project2_util.get_time()
    wday = convert_wday(x)
    hour = convert_hour(x)
    minute = convert_minute(x)

    print()
    print(("今天是%s，当前时间%.2d:%.2d") % (wday,hour,minute))

    interval = int(input("请输入一个时间间隔（分钟）："))
    min_1 = 60 * int(hour) + int(minute)
    min_2 = min_1 + interval
    day_number = (min_2 // 1440)
    wday_2 = convert_wday_2(x,day_number)

    print(("在%d分钟之后是今天之后的第%d天，那一天是%s") % (
        interval,day_number,wday_2))
    
if __name__ == '__main__':
    main()
