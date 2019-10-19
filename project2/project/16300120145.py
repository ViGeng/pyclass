import project2_util
import time
current = time.localtime()

week = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
print ('今天是%s,'%week[current.tm_wday],
       '当前时间%02d:%02d'%(current.tm_hour,current.tm_min))

t = current.tm_hour *60 + current.tm_min
interval = int (input('请输入一个时间间隔（分钟）'))
actual_tm_day = (t + interval) // 1440
(number,remainder) = divmod(actual_tm_day,7)
actual_tm_wday = current.tm_wday + remainder

print('在%d分钟之后是今天之后的第%d天,'% (interval,actual_tm_day),
      '那一天是%s'%week[actual_tm_wday])
