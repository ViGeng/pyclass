#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
import project2_util

def main():
  wday = ['','星期一','星期二','星期三','星期四','星期五','星期六','星期天']
  now = project2_util.get_time()
  now_day = now[0]
  now_hour = now[1]
  now_minute = now[2]
  print('今天是%s,当前时间%02d:%02d' % (wday[now_day],now_hour,now_minute))

  interval_minute = float(input('请输入一个时间间隔（分钟）'))
  total_minute=now_hour * 60 + now_minute + interval_minute

  interval_day = int(total_minute/1440)
  answer_day = now_day + interval_day % 7
  if(answer_day == 0):
    answer_day = 7
  print('在%d分钟之后是今天的第%d天，那一天是%s' %  (interval_minute,interval_day,wday[answer_day]))

if __name__ == '__main__':
  main()
