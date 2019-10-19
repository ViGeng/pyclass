#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
sys.path.append('D:\\University\\课件\\Python程序设计')
#需要引用的模块放在这个路径里面

import math
    
def passed_days(interval,hour,minute):
    days=(interval - 60*hour - minute)/1440
    days=math.ceil(days)
    return days


def main():
    from project2_util import get_time
    wday,hour,minute=get_time()
    from project2_util import str_wday
    '''注：str_wday这个函数的完整定义补充在引用的模块中,定义方法如下
    def str_wday(wday):
        list=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
        wday_one=list[wday-1]
        return wday_one'''
    
    wday_one=str_wday(wday)
    print("今天是",wday_one,",当前时间",hour,":",minute)
    interval=input("请输入一个时间间隔（分钟）")
    interval=int(interval)
    days=passed_days(interval,hour,minute)
    new_wday=(wday+days)%7
    wday_two=str_wday(new_wday)
    print("在",interval,"分钟之后是今天之后的第",days,"天，那一天是",wday_two)

if __name__=='__main__':
    main()
