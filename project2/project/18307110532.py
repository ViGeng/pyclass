import project2_util

A=["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
x,y,z=project2_util.get_time()
print("今天是",A[x-1],"，当前时间",y,":",z)
interval=input("请输入一个时间间隔（分钟）")
a=int(interval)+y*60+z
b=a//1440
c=(x+b)%7
print("在",interval,"分钟之后是今天之后的第",b,"天，那一天是",A[c-1])
