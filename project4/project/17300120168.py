def findrange(number):
    if number < 0 or number > 36:
        return print("编号不在[0,36]")
    elif number == 0:
        return print('编号0的pocket颜色为绿色')
    elif number <= 10 or number >=19 and number <= 28:
        if number % 2 == 0:
            print('编号%s的pocket颜色为黑色' %number)
        else:
            print('编号%s的pocket颜色为红色' %number)
    else:
        if number % 2 == 0:
            print('编号%s的pocket颜色为红色' %number)
        else:
            print('编号%s的pocket颜色为黑色' %number)

            
if __name__ == '__main__':
    number = input('请输入轮盘赌的pocket编号(0-36)==>')
    number = int(number)
    findrange(number)
