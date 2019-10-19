#!/usr/bin/env python3
# -*- coding: utf_8 -*-

from project2_util import get_time

get_time()

hour_name = get_time()[1]
min_name = get_time()[2]

if get_time()[0] == 1:
    week_name = "一"
elif get_time()[0] == 2:
    week_name = "二"
elif get_time()[0] == 3:
    week_name = "三"
elif get_time()[0] == 4:
    week_name = "四"
elif get_time()[0] == 5:
    week_name = "五"   
elif get_time()[0] == 6:
    week_name = "六"
elif get_time()[0] == 7:
    week_name = "天"
    
if min_name < 10:
    print("今天是星期" + week_name + ", 当前时间" + str(hour_name) + ":0" + str(min_name))
else:
    print("今天是星期" + week_name + ", 当前时间" + str(hour_name) + ":" + str(min_name))

print_minute = input("请输入一个时间间隔（分钟）")

tomo_minute = (24 - hour_name) * 60 - min_name

if int(print_minute) < tomo_minute:
    thatday = 0
thatday = (int(print_minute) - tomo_minute) // 1440 + 1

week_time = (get_time()[0] + thatday) % 7

if week_time == 1:
    week_name = "一"
elif week_time == 2:
    week_name = "二"
elif week_time == 3:
    week_name = "三"
elif week_time == 4:
    week_name = "四"
elif week_time == 5:
    week_name = "五"   
elif week_time == 6:
    week_name = "六"
elif week_time == 7:
    week_name = "天"

print("在" + print_minute + "分钟之后是今天之后的第" + str(thatday) +
      "天，那一天是星期" + week_name)
    
