import project2_util
time=project2_util.get_time()
wday=time[0]
if wday==1:
    x='星期一'
elif wday==2:
    x='星期二'
elif wday==3:
    x='星期三'
elif wday==4:
    x='星期四'
elif wday==5:
    x='星期五'
elif wday==6:
    x='星期六'
elif wday==7:
    x='星期日'
hour=time[1]
minute=time[2]

if int(minute)<10:
    m='0'+str(minute)
elif int(minute)>=10:
    m=str(minute)
print('今天是',x,',','当前时间',hour,':',m)
a=input('请输入一个时间间隔（分钟）')
b=int(hour)*60+int(minute)+int(a)
c=b//(24*60)
d=int(wday)+c
e=(d+int(wday))%7
if e==1:
    y='星期一'
elif e==2:
    y='星期二'
elif e==3:
    y='星期三'
elif e==4:
    y='星期四'
elif e==5:
    y='星期五'
elif e==6:
    y='星期六'
elif e==0:
    y='星期日'
print('在',a,'分钟后是今天后的第',c,'天,那一天是',y)
