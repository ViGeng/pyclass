# -*- coding: utf-8 -*-


#0-报错 1-绿色 2-红色 3-黑色 
def project_4(num):
    if num<0 or num>36:
        return 0
    elif num==0:
        return 1
    elif num>=1 and num<=10:
        if num%2==1:return 2
        else:return 3
    elif num>=11 and num<=18:
        if num%2==1:return 3
        else:return 2
    elif num>=19 and num<=28:
        if num%2==1:return 2
        else:return 3
    elif num>=29 and num<=36:
        if num%2==1:return 3
        else:return 2

def main():
    num = int(input("请输入轮盘赌的pocket编号（0-36）==>"))
    flag = project_4(num)
    if flag==0:
        print("编号不在[0,36]")
    elif flag==1:
        print("编号%d的pocket颜色为绿色" %num)
    elif flag==2:
        print("编号%d的pocket颜色为红色" %num)
    else:
        print("编号%d的pocket颜色为黑色" %num)

if __name__ == '__main__':
    main()
