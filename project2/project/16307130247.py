from project2_util import get_time
wday,hour,minute = get_time()
wday_dic = {1:'星期一', 2:'星期二', 3:'星期三', 4:'星期四', 5:'星期五', 6:'星期六', 7:'星期日'}
if minute <10:
    str_min = '0'+str(minute)
print('今天是%s，当前时间%s:%s'%(wday_dic[wday],str(hour),str_min))
time_scale = int(input('请输入一个时间间隔（分钟）'))
today_last_min = 24*60 - hour*60 - minute
remain_time = time_scale - today_last_min 
if remain_time < 0:
    print('在%d分钟之后是今天之后的第0天，那一天是%s'%(time_scale, wday_dic[wday]))
else:
    fly_day = remain_time//(24*60)+1
    fly_wday = (wday + fly_day)%7
    print('在%d分钟之后是今天之后的第%d天，那一天是%s'%(time_scale, fly_day, wday_dic[fly_wday]))