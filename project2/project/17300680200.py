import project2_util as util
wday , hour , minute = util.get_time()

today = wday % 7
day = ['星期天','星期一','星期二','星期三','星期四','星期五','星期六']
whichday = day[today]
print ('%3s%3s%5s%02d%1s%02d' %('今天是',whichday,',当前时间',hour,':',minute))

today_minute = 60 * hour + minute
interval = input('请输入一个时间间隔（分钟）')
interval = int(interval)
total_time = interval + today_minute
how_many_days_later = total_time//1440
new_date = how_many_days_later + today
new_wday = new_date % 7
new_whichday = day[new_wday]

print ('在',interval,'分钟之后是今天之后的第',how_many_days_later,'天，那一天是',new_whichday,sep = '')
