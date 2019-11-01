

def main():
    greenlist = [0]
    list1 = list(range(1,11)) + list(range(19,29))
    list2 = list(range(11,19)) + list(range(29,37))
    redlist = [r for r in list1 if r%2 == 1] + [r for r in list2 if r%2 == 0]
    blacklist = [r for r in list1 if r%2 == 0] + [r for r in list2 if r%2 == 1]

    x = int(input('请输入轮盘赌的pocket编号(0-36)==>'))

    if x in greenlist:
        print('编号%d的pocket颜色为绿色'%x)
    elif x in redlist:
        print('编号%d的pocket颜色为红色'%x)
    elif x in blacklist:
        print('编号%d的pocket颜色为黑色'%x)
    else:
        print('编号不在[0,36]')
        


if __name__=='__main__':
    main()

