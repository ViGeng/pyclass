def f1():
    i=0
    for a in range(0,20):
        for b in range(0,33):
            z=100-a-b
            if 5*a+3*b+z*1/3==100 and z%3==0:
                i+=1
                print('解%s: 鸡翁%s 鸡母%s 鸡雏%s'%(i,a,b,z))
    
def f2():
    i=0
    cock_price,hen_price,chick_price=5,3,1/3
    cock_MaxNum,hen_MaxNum,chick_MaxNum=range(0,20),range(0,33),range(0,300)
    items=[(cock,hen,chick)for cock in cock_MaxNum for hen in  hen_MaxNum for chick in  chick_MaxNum
       if int(cock*cock_price+hen*hen_price+chick*chick_price)==100 and chick%3==0 and cock+hen+chick==100]
    for c in items:
                print('     鸡翁%s 鸡母%s 鸡雏%s' % c)


f1()
f2()


