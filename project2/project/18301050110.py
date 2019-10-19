import project2_util

def weekdays(wday):
    weekdays = ['一', '二', '三', '四', '五', '六', '日']
    return weekdays[wday - 1]


def test_datetime():
    a = project2_util.get_time()
    print('今天是星期%s，当前时间%02d:%02d'%(weekdays(a[0]), a[1], a[2]))   
  
    interval = int(input('请输入一个时间间隔（分钟）'))
    t = a[1] * 60 + a[2] + interval
    d = t // 1440
    wday_d = (d + a[0]) % 7
    print('在%d分钟之后是今天之后的第%d天，那一天是星期%s' % (interval, d, weekdays(wday_d)))


if __name__ == '__main__':
    test_datetime()

    




    
    


