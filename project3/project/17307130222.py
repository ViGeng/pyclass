#!/usr/bin/env python

# -*- coding: utf-8 -*-

# File     : pj2_1.py

# Author   : Zhukaixiang 17307130222

# Date     : 2019/10/14

import project2_util

time_info = project2_util.get_time()

wday_name = [ '星期一','星期二','星期三','星期四','星期五','星期六','星期日' ]

print('今天是%s,当前时间%d:%d' %(wday_name[time_info[0]-1], time_info[1], time_info[2]))

minute = int(input('请输入一个时间间隔（分钟）'))

min_num = minute % 60  #可以计算出是未来某个时刻第几个小时的第几分钟
hour_num = (60*time_info[1]+time_info[2]+minute) // 60  #可以计算出是未来某个时刻的第几个小时
day_num = hour_num // 24  #计算出是现在时刻的多少天之后

print('在%d分钟之后是今天之后的第%d天，那一天是%s' %(minute,day_num,wday_name[(day_num+time_info[0]-1)%7]))
