
import project2_util

def Absolute_Right(interval):
    """ 调用老师所给出的验证函数：text_datetime,用于验证结果"""
    project2_util.test_datetime(interval)

def Write_via_Myself():
    wday,hour,minute = project2_util.get_time()
    a = wday
    wday = str_wday(wday)#得出今天是星期几
    print("今天是%s,"%wday,"当前时刻%2d:%0.2d"%(hour,minute))
    get_minute = float(input("请输入一个时间间隔（分钟）"))
    all_minute = get_minute + (hour * 60) + minute
    distant_day = all_minute / 1440
    #一天有1440分钟
    distant_wday = (a + distant_day) % 7
    distant_wday = str_wday(distant_wday)#得出那天是星期几
    print("在%d分钟之后是今天之后的第%d天，那一天是%s"%(get_minute , distant_day,distant_wday))   
    pass


def str_wday(wday):
    """返回中文的星期几
    wday表示本周的星期几，取值范围[1,7]，其中7表示星期天
    """
    wday_list = ['星期一', '星期二','星期三', '星期四', '星期五', '星期六', '星期日']
    num = int((wday - 1))
    wday = wday_list[num]
    return wday

def main():

    print("——我写的程序输出结果为——\n")
    Write_via_Myself()

if __name__ == '__main__':
    main()


