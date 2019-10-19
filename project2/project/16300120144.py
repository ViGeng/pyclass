import project2_util

week=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']

next_wday, current_hour, current_min = project2_util.get_time()
current_wday = next_wday - 1
print('今天是%s,'%week[current_wday], '当前时间%02d:%02d'% (current_hour, current_min))

interval_minute = int(input('请输入一个时间间隔（分钟）'))
past_time_minute = current_hour * 60 + current_min

future_day = (interval_minute + past_time_minute) // 1440
interval_wday = future_day % 7
future_wday = current_wday + interval_wday

if future_wday <= 6:
    print('在%d分钟之后是今天之后的第%d天,'% (interval_minute, future_day),'那一天是%s'%week[future_wday])
else:
    print('在%d分钟之后是今天之后的第%d天,'% (interval_minute, future_day),'那一天是%s'%week[future_wday-7])



    
   
