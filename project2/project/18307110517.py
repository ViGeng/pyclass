#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

def get_time():
    """ 返回有关当前时间的3个信息组成的元组，分别为wday, hour, minute
    wday表示本周的星期几，取值范围[1,7]，其中7表示星期天
    hour取值范围[0,23]，分钟取值范围[0,59]，表示当前时间的小时和分钟数
    """ 
    import time
    current = time.localtime()
    return current.tm_wday + 1 , current.tm_hour, current.tm_min

wday_ch=('星期一','星期二','星期三','星期四','星期五','星期六','星期日')

def str_wday(wday):
    """返回中文的星期几
    wday表示本周的星期几，取值范围[1,7]，其中7表示星期天

    """
    wday=wday_ch[wday]
    return wday

if __name__ == '__main__':    
    wday,hour,minute = get_time()
    print('今天是',str_wday(wday),',当前时间%d:%d'%(hour,minute),sep='')
    

interval = int(input('请输入一个时间间隔（分钟）'))
days=(hour*60+minute+interval)//1440
chwday=str_wday((days%7+wday)%7)

print('在',interval,'分钟之后是今天之后的第',days,'天,那一天是',sep='',end='')
print(chwday)
