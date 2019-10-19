import project2_util
wday,hour,minute = project2_util.get_time()
a=["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
print('今天是%s,当前时间%02d:%02d'%(a[wday-1],hour, minute))
interval = int(input('请输入一个时间间隔（分钟）'))
c=(((interval-((23-hour)*60)-(60-minute)))//(1440)+1)
print ('在%s分钟之后是今天之后的第%s天，那一天是%s'%(interval,c,a[(wday-1+c)%7]))
