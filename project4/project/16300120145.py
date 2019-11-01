
pocket = int(input('请输入轮盘赌的pocket编号(0-36)'))

def roulette(pocket):
    if pocket>36:
        print("编号不在[0,36]")
    elif pocket>=29 and pocket % 2 == 0:
        print('编号%d的pocket颜色为红色' % pocket)
    elif pocket>=29 and pocket % 2 != 0:
        print('编号%d的pocket颜色为黑色' % pocket)
    elif pocket>=19 and pocket % 2 != 0:
        print('编号%d的pocket颜色为红色' % pocket)
    elif pocket>=19 and pocket % 2 == 0:
        print('编号%d的pocket颜色为黑色' % pocket)
    elif pocket>=11 and pocket % 2 == 0:
        print('编号%d的pocket颜色为红色' % pocket)
    elif pocket>=11 and pocket % 2 != 9:
        print('编号%d的pocket颜色为黑色' % pocket)
    elif pocket>=1 and pocket % 2 != 0:
        print('编号%d的pocket颜色为红色' % pocket)
    elif pocket>=1 and pocket % 2 == 0:
        print('编号%d的pocket颜色为黑色' % pocket)
    else:
        print('编号%d的pocket颜色为绿色' % pocket)
   

if __name__ == '__main__':
    roulette(pocket)

