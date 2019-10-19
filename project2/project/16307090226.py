import project2_util as util

(wday,hour,minute) = util.get_time()

weekday = ['0', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
weekday_today = weekday[wday]
print('今天是%s, 当前时间%s:%s'% (weekday_today, hour, minute))

interval = float(input('请输入一个时间间隔（分钟）:'))
total_time = hour * 60 + minute + interval
days = int(total_time // (24 * 60))
interval = int(interval)
weekday_thatday = int((wday+days) % 7)
if weekday_thatday == 0 :
    weekday_thatday_chinese = weekday_today
else:
    weekday_thatday_chinese = weekday[weekday_thatday]

print('在%s分钟之后是今天的第%s天, 那一天是%s' % (interval, days, weekday_thatday_chinese))
