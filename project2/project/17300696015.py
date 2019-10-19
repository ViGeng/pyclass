import sys
sys.path.append(r"C:\Users\User\Desktop\Python")

from project2_util import get_time


def str_wday(wday):
    	wday = ['星期一','星期二','星期三','星期四','星期五','星期六','星期天']
    	return wday

    
def interv ():
    t = (current.tm_hour * 60) + (current.tm_min) - 0
    tf = (hour * 60) + (minute) - 0
    tff = ((hour * 60) + (minute) - 0)//1440
    return t,tf,tff



def main():
    print('今天是%d' %(current.tm_wday),'当前时间 %h%m' %(current.tm_hour) %(current.tm_min))
    interval = float(input('请输入一个时间间隔（分钟）'))
    a = interv.t + interval
    if a < 1440:
    print ('在%m分钟之后是今天之后的第0天' %interval)
    else:
    b = a%1440
    print ('在%m分钟之后是今天之后的第%d天' %interval %b)


if __name__ == '__main__':
    main()

    

