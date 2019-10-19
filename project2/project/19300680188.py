#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-

import project2_util

def main():
    wdaylist = ['星期日','星期一','星期二','星期三','星期四','星期五','星期六']
    wday, hour, minute = project2_util.get_time()

    print('今天是%s,当前时间%02d:%02d' % (wdaylist[wday % 7], hour, minute))
    interval = int(input('请输入一个时间间隔（分钟）'))

    t = (hour * 60 + minute +interval) // (24 * 60)
    day = (wday + t) % 7

    print('在%d分钟之后是今天之后的第%d天，那一天是%s' % (interval, t, wdaylist[day]))


if __name__ == '__main__':
    main()
