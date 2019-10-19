#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

"""
1、显示现在是星期几，当前时刻几时几分；
2、询问用户一个时间间隔（以分钟为单位）；
3、显示从现在开始过去第2步用户输入的分钟数之后的时刻是多少天之后，那一天是星期几。
"""

def print_current_time(wday, hour, minute):
    Wday = ["", "一", "二", "三", "四", "五", "六", "天"]
    print("今天是星期%s，当前时间%02d:%02d" % (Wday[wday], hour, minute)) 
    return wday, hour, minute

def calculate_interval(wday, hour, minute):
    from math import floor
    Wday = ["", "一", "二", "三", "四", "五", "六", "天"]
    interval = int(input("请输入一个时间间隔（分钟）"))
    interval_day = floor((hour * 60 + minute + interval) / 60 / 24)
    future_wday = wday + interval_day % 7
    print("在%d分钟之后是今天之后的第%d天，那一天是星期%s" % (interval, interval_day, Wday[future_wday])) 

def main():
    from project2_util import get_time
    wday, hour, minute = get_time()
    print_current_time(wday, hour, minute)
    calculate_interval(wday, hour, minute)
    #print("-------------------------------------\n以下为利用test_datetime()的测试结果\n-------------------------------------")
    #from project2_util import test_datetime
    #test_datetime()

if __name__ == '__main__':
    main()
    
    
