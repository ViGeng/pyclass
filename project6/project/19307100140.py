def chick_sol():
    total = 100
    x = []
    y = []
    z = []
    for weng in range(0,total+1):
        for mu in range(0,total+1):
            if (5 * weng + 3 * mu + 1/3 * (100 - weng - mu)) == total:
                x.append(weng)
                y.append(mu)
                z.append(100-weng-mu)
    if len(x):
        print('总共有%d个解' % (len(x)))
        for i in range(len(x)):
            print('解%d:鸡翁%d 鸡母%d 鸡雏%d' % (i+1,x[i],y[i],z[i]))
    else:
        print('无解')

def get_result():
    total = 100
    result = [[a,b,c] for a in range(total+1) for b in range(total+1) for c in range(total+1)
              if a + b + c == total and 5*a + 3*b + 1/3*c == total]
    if len(result):
        print('总共有%d个解' % (len(result)))
        for i in range(len(result)):
            print('解%d:鸡翁%d 鸡母%d 鸡雏%d' % (i+1,result[i][0],result[i][1],result[i][2]))
    else:
        print('无解')

if __name__ == '__main__':
    chick_sol()
    get_result()
