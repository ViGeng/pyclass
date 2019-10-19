from project2_util import get_time
time = get_time()
wd = time[0]
h = time[1]
m = time[2]
def wdch(wd):
    if wd == 1:
        wd = "一"
    if wd == 2:
        wd = "二"
    if wd == 3:
        wd = "三"
    if wd == 4:
        wd = "四"
    if wd == 5:
        wd = "五"
    if wd == 6:
        wd = "六"
    if wd == 7:
        wd = "天"
    if wd == 0:
        wd = "天"
    return wd
wd = wdch(wd)
print("现在是星期%s，当前时刻%s时%s分" % (wd, h, m))

lefttimetoday = (60-m)+(23-h)*60
interval = int(input("请输入一个时间间隔(分钟)"))
day = (interval - lefttimetoday)//1440 + 1
weekday = (time[0] + day) % 7
weekday = wdch(weekday)
print("在%d分钟之后是今天之后的第%d天，那一天是星期%s" % (interval, day, weekday))
