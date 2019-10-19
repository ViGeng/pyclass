#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

import project2_util

def trans(wday):
    week = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]    
    return week[wday%7 - 1]

def main():
    a = project2_util.get_time()
    print('今天是'+trans(a[0])+'，当前时间%02d:%02d'%(a[1],a[2]))
    interval = float (input('请输入一个时间间隔(分钟)'))
    import math
    b = math.floor((a[1]*60+a[2]+interval)/1440)
    print('在%d分钟之后是今天之后的第%d天，那一天是'%(interval,b)+trans(a[0]+b))
    
if __name__ == '__main__':
    main()
