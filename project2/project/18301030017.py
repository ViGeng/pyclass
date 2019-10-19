
import project2_util as pro


weekdays = ['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
wday,hour,minute = pro.get_time()
print('今天是'+weekdays[wday-1],',当前时间%02d:%02d'%(hour,minute))
interval = int(input('请输入一个时间间隔(分钟)'))
interval_day = (hour * 60 + minute + interval) // 1440
wday_next = (wday + interval_day) % 7
print('在%s分钟之后是今天之后的第%s天，那一天是%s'%(interval,interval_day,weekdays[wday_next-1]))

