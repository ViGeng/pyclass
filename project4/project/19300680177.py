def main():

    pocket = int(input("请输入轮盘赌的pocket编号(0-36)==>"))
    if pocket > 36 or pocket < 0:
        print( "编号不在[0,36]")
    elif pocket>= 29:
        if pocket %2==0:
            print("编号%d的pocket颜色为红色"%pocket)
        else:
            print("编号%d的pocket颜色为黑色"%pocket)
    elif pocket >= 19:
        if pocket %2==0:
            print("编号%d的pocket颜色为黑色"%pocket)
        else:
            print("编号%d的pocket颜色为红色"%pocket)
    elif pocket >= 11:
        if pocket %2==0:
            print("编号%d的pocket颜色为红色"%pocket)
        else:
            print("编号%d的pocket颜色为黑色"%pocket)
    elif pocket >= 1:
        if pocket %2==0:
            print("编号%d的pocket颜色为黑色"%pocket)
        else:
            print("编号%d的pocket颜色为红色"%pocket)
    else:
        print("编号%d的pocket颜色为绿色"%pocket)

if __name__ == '__main__':
    main()
