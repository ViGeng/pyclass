import math

def showcolor(num):
    if num < 0 or num > 36:
        print('编号不在[0,36]')
    elif num == 0:
        print('%s%d%s'% ('编号', num, '的pocket颜色为绿色'))
    elif 1 <= num <= 10 or 19 <= num <= 28:
        if num % 2 == 1:
            print('%s%d%s'% ('编号', num, '的pocket颜色为红色'))
        else:
            print('%s%d%s'% ('编号', num, '的pocket颜色为黑色'))
    elif 11 <= num <= 18 or 29 <= num <= 36:
        if num % 2 == 1:
            print('%s%d%s'% ('编号', num, '的pocket颜色为黑色'))
        else:
            print('%s%d%s'% ('编号', num, '的pocket颜色为红色'))
            
def main():
    num = int(input('请输入轮盘赌的pocket编号(0-36)==>'))
    showcolor(num)

if __name__ == '__main__':
    main()
