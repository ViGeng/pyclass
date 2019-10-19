from project2_util import *
tub=get_time()
cwday = ['一','二','三','四','五','六','日']
print("今天是星期",cwday[tub[0]-1],str(tub[1])+"时"+str(tub[2])+"分")
interval = int(input("请输入一个时间间隔（分钟）"))
day_after =  int ( tub[1] * 60 + tub[2] + interval )//1440
day = int(day_after+tub[0])%7
print("在",interval,"分钟后是今天之后的第",day_after,"天")
print("那一天是星期",cwday[day-1]) 
