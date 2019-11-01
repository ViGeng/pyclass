def main():
    x = int(input("请输入轮盘堵的pocket编号(0-36)==> "))
    if x > 36:
        print('编号不在[0,36]')
    else:
        if x==0:
            print('编号0的pocket颜色为绿色')
        else:
            if 1<x<10 and x % 2 == 0:
                print('编号%d的pocket颜色为黑色' % (x))
            else:
                if 11<x<18 and (x+1) % 2 == 0:
                    print('编号%d的pocket颜色为黑色' % (x))
                else:
                    if 19<x<28 and x % 2 == 0:
                        print('编号%d的pocket颜色为黑色' % (x))
                    else:
                        if 29<x<36 and (x+1) % 2 == 0:
                            print('编号%d的pocket颜色为黑色' % (x))
                        else:
                            print('编号%d的pocket颜色为黑色' % (x))


if __name__ =='__main__':
    main()
