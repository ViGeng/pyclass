def xunhuan():
    a=[]
    for x in range(0,15):
        for y in range(0,26):
            if 7*x+4*y==100:
                a.append((x,y,100-x-y))
    print("总共有%d个解"%len(a))
    for n in range(0,len(a)):
        print("解%d:鸡翁 %d 鸡母 %d 鸡雏 %d" %((n+1), a[n][0], a[n][1],a[n][2]))


def tuidao():
    a=[(x,y,100-x-y) for x in range(0,15) for y in range(0,26) if 7*x+4*y==100]
    print("总共有%d个解"%len(a))
    for n in range(0,len(a)):
        print("解%d:鸡翁 %d 鸡母 %d 鸡雏 %d" %((n+1), a[n][0], a[n][1],a[n][2]))

xunhuan()
tuidao()
    
