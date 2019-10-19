#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import project2_util as project
(wday,hour,minute) = project.get_time()


weekday = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天','7' ]
weekday_today = weekday[wday-1]
print('今天是%s, 当前时间是%0s:%0s' %(weekday_today,hour,minute))

interval = float(input('请输入一个时间间隔(单位是分钟):'))

total_minute = hour * 60 + minute + interval
days = int(total_minute // (60 * 24))

interval = int(interval)
weekday_thatday = int((wday+days)% 7)
if weekday_thatday == 0:
    weekday_thatday = weekday_today
else:
    weekday_thatday = weekday[weekday_thatday-1]


print('在%s分钟之后是今天之后的第%s天，那一天是:%s' % (interval,days,weekday_thatday))



