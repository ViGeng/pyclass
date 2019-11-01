number = int(input('请输入轮盘赌的pocket号码（0~36）==>'))
if number<0 or number>36:
    print('编号不在[0,36]')
elif number ==0:
    print('编号'+str(number)+'的pocket颜色为绿色')
elif(number%2==1)and((number >= 1 and number <=10)or(number >= 19 and number <=28)):
    print('编号'+str(number)+'的pocket颜色为红色')
elif(number%2==0)and((number >= 1 and number <=10)or(number >= 19 and number <=28)):
    print('编号'+str(number)+'的pocket颜色为黑色')
elif(number%2==1)and((number >= 11 and number <=18)or(number >= 29 and number <=36)):
    print('编号'+str(number)+'的pocket颜色为黑色')
elif(number%2==0)and((number >= 11 and number <=18)or(number >= 29 and number <=36)):
    print('编号'+str(number)+'的pocket颜色为红色')
