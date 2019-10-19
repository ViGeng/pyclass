from project2_util import get_time

wday,hour,minute=get_time()
weekday = ('星期一','星期二','星期三','星期四','星期五','星期六','星期日')

if minute <10:
    minute = '0'+str(minute)

print('今天是%s,当前时间%s：%s' % (weekday[wday],str(hour),str(minute)))

interval = int(input('请输入一个时间间隔(分钟)'))
now_to_zero = hour*60 + minute
zero_to_then = now_to_zero + interval
past_day = zero_to_then // 1440
that_day = (wday + past_day) % 7 - 1

print('在%d分钟之后是今天之后的第%d天,那一天是%s'%(interval,past_day,weekday[that_day]))
