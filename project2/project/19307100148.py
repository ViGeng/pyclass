import project2_util

from project2_util import get_time

wday,hour,minute = get_time()

from project2_util import str_wday

wdays=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']

print ('今天是'+wdays[wday-1],'当前时间'+str(hour)+str(':')+str(minute))

#'今天是%s，当前时间是%02d:%02d'

interval = float(input('请输入一个时间间隔（分钟）'))

M = int((hour*60 + minute + interval)/(60*24))

D = M % 7 + wday

print ('在%d分钟之后是今天之后的第 %d 天，那一天是%s' % (interval, M , wdays[D-1]))

if __name__ == '__main__':
    get_time()
