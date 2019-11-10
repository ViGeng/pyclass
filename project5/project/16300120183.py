# -*- coding: utf-8 -*-


def main():
    flag = 10**(10) #flag为规定极小值的倒数，此处预设为10^（-10）的倒数
    n = x = 1.0
    e = 0
    while(x <= flag):   #x为阶乘值
        e=e+(1/x)
        x=x*n
        n=n+1
    print("e =" ,e)

if __name__ == '__main__': 
    main()