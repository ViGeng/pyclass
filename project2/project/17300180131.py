import project2_util

def str_wday(wday):
    week=['星期一', '星期二', '星期三', '星期四','星期五', '星期六', '星期天]']
    current_day = week[wday-1]
    return current_day


def after_time():
    wday = project2_util.get_time()[0]
    hour = project2_util.get_time()[1]
    minute = project2_util.get_time()[2]

    current_minute = 60*hour + minute
    current_day = str_wday(wday)
    
        
    print('今天是%s,当前时间%d:%d' %(current_day, hour, minute))
    interval = float(input('请输入一个时间间隔（分钟）'))

    after_date = int((current_minute + interval)//1440 )
    after_weekday_num = int((wday + after_date) % 7)

    after_weekday = str_wday(after_weekday_num)
 
    if interval%1 == 0:
        interval = int(interval)
    else:
        interval = str(interval)
        
    print('在%s分钟之后是今天之后的第%s天，那一天是%s' %(interval, after_date, after_weekday) )
    
if __name__ == '__main__':
    after_time()
