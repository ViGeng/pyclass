
def color(number):
    if 1 <= number <= 10:
        if number % 2 == 1:
            return '红'
        if number % 2 == 0:
            return '黑'
    elif 11 <= number <= 18:
        if number % 2 == 1:
            return '黑'
        if number % 2 == 0:
            return '红'
    elif 19 <= number <= 28:
        if number % 2 == 1:
            return '红'
        if number % 2 == 0:
            return '黑'     
    elif 29 <= number <= 36:
        if number % 2 == 1:
            return '黑'
        if number % 2 == 0:
            return '红'
def main():
    number = int(input('请输入轮盘赌的pocket编号(0-36)==>'))
    if 1 <= number <=36:
        print('编号%d的pocket颜色为%s色'%(number,color(number)))
    else :
        print('编号不在[0,36]')
        
if __name__ == '__main__':
    main()



