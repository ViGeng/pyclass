#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

from project2_util import get_time

chinese_num = ['一', '二', '三', '四', '五', '六', '天']
time        = get_time()
today_wday  = chinese_num[time[0] -1]
today_min   = time[1] * 60 + time[2]

print('今天是星期%s，当前时间%d:%d'
      %(today_wday, time[1], time[2]))

interval    = input('请输入一个时间间隔（分钟）')
interval    = int(interval)
future_min  = today_min + interval
day_pass    = int(future_min / 1440)
wday_num    = (time[0] + day_pass) % 7
future_wday = chinese_num[wday_num -1]
#特别地当time[0]+day_pass被7整除时，wday_num-1=-1仍能取出‘天’这倒数第一个汉字

print('在%d分钟后是今天之后的第%d天，那一天是星期%s'
      %(interval, day_pass, future_wday))
