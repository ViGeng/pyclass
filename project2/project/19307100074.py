import project2_util

wday,hour,minute = project2_util.get_time()
week=['一','二','三','四','五','六','天']
wday_=week[wday-1]
hour_=str(hour)
minute_=str(minute)
print('今天是星期'+wday_+'，当前时间'+hour_+':'+minute_)

import math
time_=input('请输入一个时间间隔（分钟）:')
last=24*60-hour*60-minute
time=int(time_)
show=(time-last)//1440+1
show_=str(show)
show2=(wday+show)%7
show2_=week[show2-1]
print('在'+time_+'分钟之后是今天之后的第'+show_+'天，那一天是星期'+show2_)

#project2_util.test_datetime()
