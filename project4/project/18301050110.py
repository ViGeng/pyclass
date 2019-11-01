pocket = input("请输入轮盘赌的pocket编号（0-36）==>")
pocket = int(pocket)
if pocket > 36 or pocket < 0:
    print ('编号不在[0,36]')
elif pocket == 0:
    print ('编号%d的pocket颜色为绿色' % (pocket))
elif (pocket >= 1 and pocket <= 10) or (pocket >= 19 and pocket <= 28):
    if pocket // 2 == 0:
        print ('编号%d的pocket颜色为黑色' % (pocket))
    else:
        print ('编号%d的pocket颜色为红色' % (pocket))
elif (pocket >= 11 and pocket <=18) or (pocket >= 29 and pocket <= 36):
    if pocket // 2 == 0:
        print ('编号%d的pocket颜色为红色' % (pocket))
    else:
        print ('编号%d的pocket颜色为黑色' % (pocket))
        
