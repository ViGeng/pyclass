k = int(input('请输入轮盘赌的pocket编号'))
if k == 0:
 print( '编号0的颜色为绿色')
else:
    if k > 36 or k < 0:
     print('编号不在[0,36]')
    else:
         if k > 0 and k < 11 and k % 2 == 0:
             print('编号%d的pocket颜色为黑色' % k )
         else:
                 if k > 0 and k < 11 and k % 2 == 1:
                     print('编号%d的pocket颜色为红色' % k )
                 else:
                        if k > 10 and k < 19 and k % 2 == 0:
                           print('编号%d的pocket颜色为红色' % k )
                        else:
                              if k > 10 and k < 19 and k % 2 == 1:
                                 print('编号%d的pocket颜色为黑色' % k )
                              else:
                                     if k > 18 and k < 29 and k % 2 == 0:
                                        print('编号%d的pocket颜色为黑色' % k )
                                     else:
                                           if k > 18 and k < 29 and k % 2 == 1:
                                             print('编号%d的pocket颜色为红色' % k )
                                           else:
                                                   if k > 28 and k < 37 and k % 2 == 0:
                                                      print('编号%d的pocket颜色为红色' % k )
                                                   else:
                                                      if k > 28 and k < 37 and k % 2 == 1:
                                                         print('编号%d的pocket颜色为黑色' % k )
     

