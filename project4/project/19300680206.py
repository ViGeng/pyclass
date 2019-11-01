t = float(input('请输入轮盘赌的pocket编号(0—36)==>'))

if t == 0:
    print("编号%.0f的pocket颜色为绿色" % (t))
elif 1 <= t <= 10 or 19 <= t <= 28:
    if t % 2 == 0:
        print("编号%.0f的pocket颜色为黑色" % (t))
    if t % 2 == 1:
        print("编号%.0f的pocket颜色为红色" % (t))
elif 11 <= t <= 18 or 29 <= t <= 36:
    if t % 2 == 0:
        print("编号%.0f的pocket颜色为红色" % (t))
    if t % 2 == 1:
        print("编号%.0f的pocket颜色为黑色" % (t))
else:
    print("编号不在[0,36]")
