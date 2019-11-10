


def main(delta=15):
    e = 0
    k = 0
    fac = 1

    while k <= delta + 10:
        e += 1/fac
        k += 1
        fac *= k

    return e

def deci(x,n=1):
##   对一个浮点数x输出n位小数后的形式
##   例如x=pi,n=3输出3.141
    
    n = int(n)
    x_d = int(x)
    print(x_d,sep = '',end = '.')
    x_1 = float(x) - x_d
    for i in range(n):
        x_1 = 10 * x_1
        k = int(x_1)
        print(k,sep = '',end = '')
        x_1 = x_1 - k
    else:
        print()
        
    


if __name__=='__main__':
    delta = int(input('保留小数点后N位，N='))
    print('自然对数e保留%d位小数为'%delta,sep = '',end = '')
    deci(main(delta),delta)

