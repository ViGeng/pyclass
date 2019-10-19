import project2_util as util
wday, hour, minute = util.get_time()
aList = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期六', '星期天']
t = wday - 1 
nowwday = aList[t] #把数字转换变为汉字的星期几


def main():
    print('今天是%s,当前时间%d:%d' % (nowwday, hour, minute))
    target = input('请输入一个时间间隔（分钟）')
    target = int(target)
    passminutes = 60 * hour + minute  #求当前时刻距离今天0点过去了多少分钟
    interval = passminutes + target   # 求出interval的总值
    daydistance = interval // 1440    #求出interval对应的天数
    transition = daydistance // 7      
    change = daydistance - 7 * transition
    waday = util. get_time()
    bList = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期六', '星期天']
    t = wday + change - 1
    futurewday = bList[t]
    print('在%d分钟之后是今天之后的第%d天, 那一天是%s' % (target, daydistance, futurewday))

    

if __name__ == '__main__':
    main()
