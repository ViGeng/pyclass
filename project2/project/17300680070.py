import project2_util as util

wday, hour, min = util.get_time()
weekday = wday - 1
s = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']
nowweekday = s[weekday]

import math
print('%3s%3s%5s%02d%1s%02d' %('今天是', nowweekday, ',当前时间', hour, ':', min))

deltatime = input('请输入一个时间间隔（分钟）')
deltatime = float(deltatime)
deltatime = math.floor(deltatime)
deltaday = deltatime + hour * 60 + min
deltaday = deltaday // 1440
date = wday + deltaday
date = date % 7
date = date - 1
futureweekday = s[date]
print('在', deltatime, '分钟之后是今天之后的第', deltaday, '天，那一天是', futureweekday, sep = "")
