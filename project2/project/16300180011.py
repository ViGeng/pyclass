##作业2 2019-10-11


import project2_util as p2

def dateoutput(wday,hour,minute):
    daylist = ['天','一','二','三','四','五','六']
    print('今天是星期%s，当前时间是%d:%d'%(daylist[wday % 7],hour,minute))

def interval(deltaT,wd,h,m):
    daylist = ['天','一','二','三','四','五','六']
    deltaD = ((m + deltaT) // 60 + h) // 24
    Days = int((wd + deltaD) % 7)
    print('在%d分钟之后是今天之后的第%d天，那一天是星期%s'%(deltaT,deltaD,daylist[Days]))

def main():
    wday,hour,minute=p2.get_time()
    dateoutput(wday,hour,minute)
    deltaT = float(input('请输入一个时间间隔（分钟）'))
    interval(deltaT,wday,hour,minute)


if __name__ == '__main__':
    main()
##    input('press any key...')
