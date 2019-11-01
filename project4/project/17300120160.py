if __name__=='__main__':
        
        a=int(input('请输入轮盘赌的pocket编号[0,36]' ))
        if a < 0 or a > 36:
                print("编号不在[0,36]")
        elif a==0:
                print('编号'+str(a)+'号的pocket颜色为绿色')
        elif a<11 or(18<a<29):
                if a%2==0:
                        print('编号'+str(a)+'号的pocket颜色为黑色')
                else:
                        print('编号'+str(a)+'号的pocket颜色为红色')
        else:
                if a%2==0:
                        print('编号'+str(a)+'号的pocket颜色为红色')
                else:
                        print('编号'+str(a)+'号的pocket颜色为黑色')
