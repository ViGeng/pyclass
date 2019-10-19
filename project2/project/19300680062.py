#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
#project2 作者：19级经济学院 应眺

import project2_util

weekdays=('星期一','星期二','星期三','星期四','星期五','星期六','星期日')

def time1():
    gettime=project2_util.get_time()
    wday = weekdays[gettime[0]-1]
    hour = gettime[1]
    minute = gettime[2]
    if minute < 10:
        minute = '0'+ str(minute)
    print('今天是',wday,',当前时间',hour,':',minute,sep='')
    time2()


def time2():
    gap=input('请输入一个时间间隔（分钟）')
    gettime=project2_util.get_time()
    wday = weekdays[gettime[0]-1]
    hour = gettime[1]
    minute = gettime[2]
    day = (int(hour*60)+int(minute)+int(gap))//1440
    if (gettime[0]+day)%7 == 0:
        wday2 = 7
    else:
        wday2 = (gettime[0]+day)%7
    print('在',gap,'分钟之后是今天之后的第',day,'天，那一天是', \
          weekdays[wday2-1],sep='')


if __name__ == '__main__':
    time1()
