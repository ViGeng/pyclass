import project2_util
wday,hour,minute = project2_util.get_time()
a = ["星期一","星期二","星期三","星期四","星期五","星期六","星期天"]
print("今天是",a[wday-1],"，当前时间",hour,":",minute)
time = int(input("请输入一个时间间隔（分钟）"))
days = (hour*60 + minute +time)//(60*24)
new_wday = (wday + days)%7
print("在",time,"分钟之后是今天之后的第",days,"天，那一天是",a[new_wday -1])
