def f(money=100,number=100):
    i=0
    u=1
    list=[]
    for old in range(0,number+1):
        for hen in range(0,number+1):
            for chick in range(0,number+1):
                if ((old+hen+chick)==number and (5*old+3*hen+chick/3)==money):
                    list.insert(i,old)
                    i=i+1
                    list.insert(i,hen)
                    i=i+1
                    list.insert(i,chick)
                    i=i+1
    print("总共有",int(i/3),"个解")
    while u<=i/3:
        print("解",u,":鸡翁",list[u*3-3],"鸡母",list[u*3-2],"鸡雏",list[u*3-1])
        u=u+1
f(100,100)
        
                    
