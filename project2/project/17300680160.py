#  -*- coding: utf-8 -*-

import project2_util

def now_time():
	wday, hour, mine = project2_util.get_time()
#    print(wday,hour,min)
	print("今天是星期",project2_util.str_wday(wday),",当前时间 %d:%d" %(hour,mine))

def interval_time():
	wday, hour, mine = project2_util.get_time()
	interval = float(input('请输入一个时间间隔（分钟）'))
	past_day = interval//1440
	past_min = interval%1440
	if(past_min>=(1440-60*hour-mine)):
		past_day += 1
	new_wday = (wday + past_day%7)%6
	print("在%d分钟之后是今天之后的第%d天，那一天是星期" %(interval,past_day), end="")
	print(project2_util.str_wday(int(new_wday)))

if __name__=="__main__":
	now_time()
	interval_time()
