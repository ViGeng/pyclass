def color(number):
    if number < 0 or number > 36:
        print("编号不在[0,36]")
    elif number == 0:
        print("编号%d的pocket颜色为绿色" % number)
    elif 1<= number <= 10 or 19 <= number <= 28:
        if number % 2 == 0:
            print("编号%d的pocket颜色为黑色" % number)
        else:
            print("编号%d的pocket颜色为红色" % number)
    elif number % 2 == 0:
        print("编号%d的pocket颜色为红色" % number) 
    else:
        print("编号%d的pocket颜色为黑色" % number)    
        
    

if __name__ == '__main__':
    number = int(input("请输入轮盘赌的pocket编号(0-36)==>"))
    color(number)

        
