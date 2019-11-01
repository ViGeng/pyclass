# -*- coding: utf-8 -*-
def main():
    number = int(input("请输入轮盘赌的pocket编号（0-36）==>"))
    if number == 0:
        print('编号%d的pocket颜色为绿色'%number)
    elif number >0 and number <=10:
        if number%2 ==0:
            print('编号%d的pocket颜色为黑色'%number)
        else:
            print('编号%d的pocket颜色为红色'%number)
    elif number >=11 and number <=18:
        if number%2 ==0:
            print('编号%d的pocket颜色为红色'%number)
        else:
            print('编号%d的pocket颜色为黑色'%number)
    elif number >=19 and number <=28:
        if number%2 ==0:
            print('编号%d的pocket颜色为黑色'%number)
        else:
            print('编号%d的pocket颜色为红色'%number)
    elif number >=29 and number <=36:
        if number%2 ==0:
            print('编号%d的pocket颜色为红色'%number)
        else:
            print('编号%d的pocket颜色为黑色'%number)
    else:
        print("编号不在[0,36]")

if __name__ == '__main__':
    main()
    