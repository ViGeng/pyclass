days = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
import project2_util
wday,hour,minute = project2_util.get_time()
print('今天是%s,当前时间%d:%d'%(days[wday-1],hour,minute))
interval = int(input('请输入一个时间间隔（分钟）'))
time = interval + hour*60 + minute
t1 = time // 1440
t2 = wday + t1 % 7
if(t2 > 7):
    t2 = t2 - 7   
print('在%d分钟之后是今天之后的第%d天，那一天是%s'%(interval,t1,days[t2-1]))

