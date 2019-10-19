import project2_util as util
wday,hour,minute=util.get_time()


def f():
    week=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']
    chinese_wday=week[wday-1]
    print('今天是%s,当前时间是%d:%d' % (chinese_wday,hour,minute))
    minute_add=int(input('请输入一个时间间隔（分钟）'))
    minute_length=(hour*60+minute+minute_add)/(24*60)
    pass_day=int(minute_length)
    day=(wday+pass_day)%7
    weekday=week[day-1]
    print('在%d分钟之后是今天之后的第%d天，那一天是%s' % (minute_add,pass_day,weekday))

f()

      
