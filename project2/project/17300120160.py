from project2_util import get_time

if __name__=='__main__':
    s = get_time()

    a = ['0', '一', '二', '三', '四', '五', '六', '天']

    day = s[0]
    hour = s[1]
    minute = s[2]
    n = a[day]

    print('今天是星期' + n + '，当前时间' + str(hour) + ':' + str(minute))

    interval = int(input('请输入一个时间间隔（分钟）'))
    t = hour*60 + minute + interval
    days = t//1440

    dayslater = (days + day) % 7
    if dayslater == 0:
        dayslater = 7

    print('在' + str(interval) + '分钟之后是今天之后的第' + str(days) + '天，那一天是星期' + a[(dayslater)])
 
