#数字转化为汉字

#导入模块（路径/目录）
import sys
sys.path

import project2_util
project2_util.get_time()

#进行字典设置
b = {1:'星期一',2:'星期二',3:'星期三',4:'星期四',5:'星期五',6:'星期六',7:'星期天'}
c = project2_util.get_time()
print( "今天是%s, 当前时间为%s:%s" % (b[c[0]],c[1],c[2]))


#输入时间间隔
interval = float(input('请输入一个时间间隔（分钟）'))
time1 = (c[1]*60)+c[2]

#到今天过了几天？
time2 = int(((time1+interval)/60)//24)

#那一天是星期几？
time3 = (c[0]+time2) % 7

#再次进行字典设置
d = {1:'星期一',2:'星期二',3:'星期三',4:'星期四',5:'星期五',6:'星期六',0:'星期天'}

print( "在%.0f分钟后是今天之后的%.0f天,那一天是%s" % (interval,time2,d[(time3)]))




