def hundred_chick(chick = 100, cost = 100):
    Found = False
    result = []
    for rooster in range(0,chick+1):
        for hen in range(chick+1):
            for chicken in range(chick+1):
                if chicken % 3 == 0 and rooster*5 +hen*3 + chicken/3 == cost and rooster + hen + chicken == chick:
                    answer=(rooster,hen,chicken)
                    result.append(answer)
                    Found = True
                    break
                
    print('总共有%d个解'%len(result))
    for i in result:
        print('解%d: 鸡翁%d 鸡母%d 鸡雏%d'%((result.index(i)+1),*i))
            
    if not Found:
        print('无解')                   
    return
                

def get_hundred_chick():
    result=[(rooster, hen, chicken) for rooster in range(101) for hen in range(101) for chicken in range(101)
            if chicken % 3 == 0 and rooster*5 +hen*3 + chicken/3 == 100 and rooster + hen + chicken == 100]
    
    print('总共有%d个解'%len(result))
    for i in result:
        print('解%d: 鸡翁%d 鸡母%d 鸡雏%d'%((result.index(i)+1),*i))
            
    if result==[]:
        print('无解')                   
    return

        

if __name__ =='__main__':
    hundred_chick(chick = 100, cost = 100)
    print('-'*30)
    get_hundred_chick()

