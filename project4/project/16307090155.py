def number(pocket):
    pocket = int(input("请输入轮盘赌的pocket编号(0-36) ==> "))
    return (pocket)

if __name__ == '__main__':
    print()
    
    pocket = int(input("请输入轮盘赌的pocket编号(0-36) ==> "))
    
    if pocket > 37 or pocket < 0:     
        print("编号不在[0,36]")
        
    elif pocket == 0:
        print("编号为%.f的pocket颜色为绿色" % pocket)

    elif pocket % 2 ==0 and (10 >= pocket >=1 or 28 >= pocket >=19):
        print("编号%.f的pocket颜色为黑色" % pocket)

    elif pocket % 2 ==1 and (18 >= pocket >=11 or 36 >= pocket >=29):
        print("编号%.f的pocket颜色为黑色" % pocket)

    else:
        print("编号%.f的pocket颜色为红色" % pocket)


 
    

