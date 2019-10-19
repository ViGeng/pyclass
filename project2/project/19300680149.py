import project2_util as util
weekdays=['星期一','星期二','星期三','星期四','星期五','星期六','星期日']

def time1():
    nowtime=util.get_time()
    day=weekdays[nowtime[0]-1]
    hour=nowtime[1]
    minute=nowtime[2]
    print('今天是',day,',当前时间',hour,':',minute,sep='')
    time2()

def time2():
    nowtime=util.get_time()
    interval=input('请输入一个时间间隔(分钟)：')
    day=weekdays[nowtime[0]-1]
    hour=nowtime[1]
    minute=nowtime[2]
    alltime=int(hour*60+minute+int(interval))
    daytwo=alltime//1440
    d=daytwo%7
    if d==0:
        day3=weekdays[nowtime[0]-1]
    else:
        day3=weekdays[nowtime[0]-1+(daytwo)%7]
    print ('在',interval,'分钟后是今天之后的第',daytwo,'天，','那一天是',day3,sep='')

if __name__ == '__main__':
    time1()



