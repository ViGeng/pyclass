#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import project2_util
(wday,hour,minute)=project2_util.get_time()
list=['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
print('今天是',list[wday-1],',','当前时间',hour,':',minute,sep='')

interval=int(input('请输入一个时间间隔（分钟）'))
m = (60 * hour + minute + interval) // 1440
#计算interval分钟后那一天是今天之后的第几天
n = (60 * hour + minute + interval) % 1440
#计算interval分钟后是那一天的第几分钟
wday = (wday + m) % 7
#计算interval分钟后是那一周的第几天

print('在',interval,'分钟之后是今天之后的第',m,'天',',','那一天是',list[wday-1],sep='')



