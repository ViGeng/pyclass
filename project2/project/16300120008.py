# -*- coding: utf-8 -*-
"""

"""

import project2_util as p

def func():
    tup=("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    
    wday,hour,minute = p.get_time()
    print("今天是%s，当前时间%02d:%02d" %(tup[wday-1],hour,minute))
    minu = int(input("请输入一个时间间隔（分钟）"))
    minute_0 = minute + hour*60
    days = (minute_0 + minu) // (24*60) 
    week = (days + wday) % 7    
    print("在%d分钟之后是今天之后的第%d天，那一天是%s" %(minu,days,tup[week-1]))

def main():
    func()
    
if __name__ == "__main__":
    main()
