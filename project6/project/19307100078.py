def f1():
    alist = []
    for i in range (0,int(100/5 + 1)):
        for n in range (0,int((100 - 5*i)/3) + 1):
             m = 3*(100 - 5*i - 3*n)
             if i + n + m == 100:
                alist.append([i,n,m])

    l = len(alist)
    print('总共有%d个解'%l)
    for x in range(0,l):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' %((x+1),alist[x][0], alist[x][1],alist[x][2]))

def f2():
    alist = [[x,y,z] for x in range(int(100/5 + 1))
             for y in range(int(100/3) + 1)
             for z in range(100 + 1) if x+y+z == 100 and 5*x + 3*y + z/3 == 100]
    l = len(alist)
    print('总共有%d个解'%l)
    for x in range(0,l):
       print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' %((x+1),alist[x][0], alist[x][1],alist[x][2]))
       
if __name__ == '__main__':
    f1()
    f2()
