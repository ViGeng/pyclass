#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

#显示当前的星期和时刻
import project2_util
(wday,hour,minute)=project2_util.get_time()
listweekday=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
weekday=listweekday[(wday-1)]
print('今天是%s，当前时间%d：%d' %(weekday,hour,minute))

#输入间隔并计算
interval=input('请输入一个时间间隔（分钟）')
interval=int(interval)
minutes=hour*60+minute
day=(minutes+interval)//(24*60)
weekday1=listweekday[((wday+day)%7)-1]
print('在%d分钟之后是今天之后的第%d天，那一天是%s' %(interval,day,weekday1))

if __name__ == '__main__':
    main()
