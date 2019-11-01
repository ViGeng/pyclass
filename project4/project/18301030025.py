x = input("请输入轮盘赌的pocket编号（0-36） ==> ")  
x = float(x)

if x>36:
    n = 0
elif x>=29:
    if x %2==0:
        n = 1
    else:
       n = 2    
elif x>=19:
    if x%2==0:
        n = 2
    else:
        n = 1
elif x>=11:
    if x%2==0:
        n = 1
    else:
        n = 2
elif x>=1:
    if x%2==0:
        n = 2    
    else:
        n = 1
elif x==0:
    n = 3
else:
    n = 0


if n==0:
    print('编号不在[0,36]')
elif n==1:
    print("编号%.f的pocket颜色为红色" % x)
elif n==2:
    print("编号%.f的pocket颜色为黑色" % x)
else:
    print("编号%.f的pocket颜色为绿色" % x)

    
    


