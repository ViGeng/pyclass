def computeChicken():
    x=[]
    for cock in range(0, 21):
        for hen in range(0,34):
            biddy = 100 - cock - hen
            if ((cock + hen + biddy) == 100
                and (cock * 5 + hen * 3 + biddy /3) == 100):
                    x.append([cock,hen,biddy])                    
    print('总共有四个解')
    for i,x in enumerate(x,1):
        
        print('解',i ,':','鸡翁%d, 鸡母%d, 鸡雏%d'% (x[0],x[1],x[2]))

computeChicken()               


def computeChicken111():    
    r= [[i,j,(100-i-j)] for i in range(0,21)  for j in range(0,34) 
              if i*5 +j*3 + (100-j-i)/3 == 100 ]
    print('总共有四个解')
    for i,r in enumerate(r,1):
        print('解',i ,':','鸡翁%d, 鸡母%d, 鸡雏%d'% (r[0],r[1],r[2]))

computeChicken111()      
