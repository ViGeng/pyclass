               #没有搞懂怎么调用所以选择了复制粘贴大法
def get_time():
    """ 返回有关当前时间的3个信息组成的元组，分别为wday, hour, minute
    wday表示本周的星期几，取值范围[1,7]，其中7表示星期天
    hour取值范围[0,23]，分钟取值范围[0,59]，表示当前时间的小时和分钟数
    """ 
    import time
    current =time.localtime()
    return current.tm_wday + 1 , current.tm_hour, current.tm_min

def str_wday(wday):                        #改写为中文星期
    list_day = ['星期天','星期一','星期二','星期三','星期四','星期五','星期六','星期天']
    return list_day[wday]
    
def day_interval(hour,minute,interval):    #计算今天之后的第几天
	daynumber = (int(hour)*60+int(minute)+int(interval))//1440
	return daynumber

def change_wday(wday,daynumber):          #计算几天之后是星期几
	changedwday = (wday+daynumber)%7
	return changedwday
	
    
def main():
	wday,hour,minute = get_time()
	print("今天是"+str_wday(wday)+",当前时间是"+str(hour)+":"+str(minute))
	interval = input("请输入一个时间间隔(分钟):")
	daynumber = day_interval(hour,minute,interval)
	wdaynumber = str_wday(change_wday(wday,daynumber))
	print("在"+str(interval)+"分钟之后是今天之后的第"+str(daynumber)+"天"+",那一天是"+str(wdaynumber))
	
if __name__ == '__main__':
	main()  

