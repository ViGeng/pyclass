#-------------------------------------------------------------------------------
# Name:        星期几
# Purpose:     显示现在是星期几，并在用户输入时间间隔（分钟）后显示分钟数之后的时刻是多少天之后，那一天是星期几
#
# Author:      徐思源
#
# Created:     17/10/2019
# Copyright:   (c) XU 2019
# Licence:     17307110356
#-------------------------------------------------------------------------------

#!/usr/bin/env python3
#  -*- coding: utf-8 -*-e

def main():
    import project2_util as util
    now_time = util.get_time()                                                   #星期x，x点x分
    week_nums = '一二三四五六日'                                                 #一周星期列表
    now_day = week_nums[now_time[0] - 1]                                           #输出星期几
    now_hour = now_time[1]
    now_min = now_time[2]

    print('今天是星期' + str(now_day) + \
        '，当前时间' + str(now_hour) + ':' + str(now_min))


    time_interval = input('请输入一个时间间隔（分钟）：')
    after_time = int(now_hour) * 60 + int(now_min) + int(time_interval)          #整数化
    day_interval = after_time // 1440
    after_day = week_nums[(now_time[0] + day_interval) % 7 - 1]
    after_hour = after_time % 1440 // 60
    after_min = after_time % 1440 % 60

    print('在{}分钟后是今天之后的第{}天，那一天是星期{}*时刻为{}:{}' \
        .format(time_interval, day_interval, after_day, after_hour, after_min))



if __name__ == '__main__':
    main()









