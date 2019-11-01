x = int (input("请输入轮盘赌的pocket编号（0—36）==> ") )
if x == 0:
 print ("编号为%s的pocket颜色为绿色" % (x))

elif 0<x<11 and x % 2 == 0 :
         print ("编号为%s的pocket颜色为黑色" % (x))

elif 0<x<11 and x % 2 != 0:
         print ("编号为%s的pocket颜色为红色" % (x))

elif 10<x<19 and x % 2 == 0:
         print ("编号为%s的pocket颜色为红色" % (x))

elif 10<x<19 and x % 2 != 0:
         print ("编号为%s的pocket颜色为黑色" % (x))

elif 18<x<29 and x % 2 == 0:
         print ("编号为%s的pocket颜色为黑色" % (x))

elif 18<x<29 and x % 2 != 0:
         print ("编号为%s的pocket颜色为红色" % (x))

elif 28<x<37 and x % 2 == 0:
         print ("编号为%s的pocket颜色为红色" % (x))

elif 28<x<37 and x % 2 != 0:
         print ("编号为%s的pocket颜色为黑色" % (x))

else :
         print('编号不在[0，36]')
            


