#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

# Project 2 星期几
# 宋德夫（17307110044）

import project2_util

def current_time():
    week = ("一","二","三","四","五","六","天")
    hour = float(project2_util.get_time()[1])
    minute = float(project2_util.get_time()[2])
    print("今天是星期" + week[project2_util.get_time()[0]-1] +
          "，当前时间" + "%02.f" % hour + ":" + "%02.f" % minute)

def interval(x):
    week = ("一","二","三","四","五","六","天")
    minutes = project2_util.get_time()[1] * 60 + project2_util.get_time()[2] + x
    days = minutes // 1440
    weeks = (project2_util.get_time()[0] + days) % 7
    print("在" + str(int(x)) + "分钟之后是今天之后的第" + str(int(days)) +
          "天，那一天是星期" + week[int(weeks - 1)])

def main():
    current_time()
    x = input("请输入一个时间间隔（分钟）")
    x = float(x)
    interval(x)

if __name__ == "__main__":
    main()
