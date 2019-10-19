#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import project2_util

wday = project2_util.get_time()[0]
hour = project2_util.get_time()[1]
minute = project2_util.get_time()[2]

if 0 <= minute < 10:
   minute = str(0) + str (minute)

wday_display = ""
time_display = str(hour)+":"+str(minute)

if wday == 1:
    wday_display = "星期一"
elif wday == 2:
    wday_display = "星期二"
elif wday == 3:
    wday_display = "星期三"
elif wday == 4:
    wday_display = "星期四"
elif wday == 5:
    wday_display = "星期五"
elif wday == 6:
    wday_display = "星期六"
else:
    wday_display = "星期天"

print("今天是%s, 当前时间%s" % (wday_display, time_display))


a = input("请输入一个时间间隔（分钟）")
now_minute = hour * 60 + minute
next_minute = now_minute + int(a)
next_day = next_minute // (24 * 60)
next_wday = (next_day + wday) % 7

if(next_wday == 0):
    next_wday = 7

if next_wday == 1:
    next_wday_display = "星期一"
elif next_wday == 2:
    next_wday_display = "星期二"
elif next_wday == 3:
    next_wday_display = "星期三"
elif next_wday == 4:
    next_wday_display = "星期四"
elif next_wday == 5:
    next_wday_display = "星期五"
elif next_wday == 6:
    next_wday_display = "星期六"
else:
    next_wday_display = "星期天"

print("在%s分钟之后是今天之后的第%s天，那一天是%s" % (a, next_day, next_wday_display))


