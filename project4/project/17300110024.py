number=eval( input('请输入轮盘赌的pocket编号(0-36)==>') )

if number<0 or number>36:
    print('编号不在[0,36]')

elif number == 0:
   print ('编号%d的pocket颜色为绿色'%number)

elif 1 <= number <= 10:
   if number%2 == 0:
      print ('编号%d的pocket颜色为黑色'%number)
   else:
      print ('编号%d的pocket颜色为红色'%number)

elif 11 <= number <= 18:
   if number%2 == 0:
      print ('编号%d的pocket颜色为红色'%number)
   else:
      print ('编号%d的pocket颜色为黑色'%number)

elif 19 <= number <= 28:
   if number%2 == 0:
      print ('编号%d的pocket颜色为黑色'%number)
   else:
      print ('编号%d的pocket颜色为红色'%number)

elif 29 <= number <= 36:
   if number%2 == 0:
      print ('编号%d的pocket颜色为红色'%number)
   else:
       print ('编号%d的pocket颜色为黑色'%number)
