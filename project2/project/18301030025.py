import project2_util
get_time = project2_util.get_time()
wday,hour,minute = get_time
wday = wday-1 # [1,7], 7表示星期天 
weekdays = ('星期一','星期二','星期三','星期四','星期五','星期六','星期天')

print('今天是%s,当前时间%02d:%02d' % (weekdays[wday],hour,minute))

interval = float(input('请输入一个时间间隔（分钟）'))
t = interval+60*hour+minute-24*60
t = t/60
import math
t = math.ceil(t)
t = t/24
t = math.ceil(t)
wday = (wday+t) %7
weekdays = ('星期一','星期二','星期三','星期四','星期五','星期六','星期天')
print('在%d分钟之后是今天的第%d天，那一天是%s' % (interval,t,weekdays[wday]))
