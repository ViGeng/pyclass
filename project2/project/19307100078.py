import project2_util
project2_util.get_time()
wday = (project2_util.get_time()[0])
hour = (project2_util.get_time()[1])
minute = (project2_util.get_time()[2])
chinesewday = [ '星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
print('今天是%s，当前时间为%02d:%02d'%(chinesewday[wday-1],hour, minute))

interval = int(input('请输入一个时间间隔（分钟）'))
day = (interval + hour*60 + minute) // (24*60)
wday2 = (day + wday) % 7
print('在%d分钟之后是今天之后的第%d天，那一天是%s'%(interval,day,chinesewday[wday2-1]))
