import project2_util as util

wday, hour, minute = util.get_time()

s1 = [1, 2, 3, 4, 5, 6, 7]
s2 = ['一', '二', '三', '四', '五', '六', '天']

wday = s1.index(wday)

print('今天是星期', s2[wday],'，当前时间', hour,':', minute)

add = float(input('请输入一个时间间隔(分钟)'))
total = hour * 60 + minute + add
day = (total - (total % 1440)) / 1440
wek = (day + wday) % 7 + 1

wek = s1.index(wek)

print('在%.0f'% add, '分钟后是今天之后的第%.0f'% day, '天，那一天是星期', s2[wek])
