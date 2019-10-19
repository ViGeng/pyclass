import project2_util

def main():
    
    wday = ['','星期一','星期二','星期三','星期四','星期五','星期六','星期天']
    now = project2_util.get_time()
    now_day = now[0]
    now_hour = now[1]
    now_min = now[2]
    print('今天是%s,当前时间%02d:%02d' % (wday[now_day],now_hour,now_min))

    interval_min = float(input('请输入一个时间间隔(分钟)'))
    total_min = now_hour * 60 + now_min + interval_min
    interval_day = int(total_min / 1440)

    answer_day = (now_day + interval_day) % 7
    if answer_day == 0:
        answer_day = 7
    
    print('在%d分钟之后是今天之后的第%d天，那一天是%s' % (interval_min, interval_day,wday[answer_day]))
    
if __name__ == '__main__':
    main()
    
