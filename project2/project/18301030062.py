'''显示现在是星期几，当前时刻几时几分。
询问用户一个时间间隔，显示从现在开始经过该时间间隔之后的时刻是多少天之后，那一天是星期几。'''



import project2_util as p


weekdays = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
wday_now,hour_now,minute_now = p.get_time()
print('今天是'+weekdays[wday_now-1],',当前时间%02d:%02d'%(hour_now,minute_now))
interval = int(input('请输入一个时间间隔(分钟)'))
interval_day = (hour_now * 60 + minute_now + interval) // 1440
wday_next = (wday_now + interval_day) % 7
print('在%s分钟之后是今天之后的第%s天，那一天是'%(interval,interval_day)+weekdays[wday_next-1])
