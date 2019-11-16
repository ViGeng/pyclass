def cock_hen_chicken( ):

    answer = []
    for cocks in range(100//5 +1 ): 
        for hens in range((100-cocks*5)//3 + 1):
            if 7 *cocks+ 4 * hens == 100:    
                answer.append((cocks,hens,100-cocks-hens))

    print('总共有%d个解' % len(answer))
    for num,value in enumerate(answer,1):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % (num, *value))

def cock_hen_chicken_all( ):

    answer = [ (cocks,hens,100-cocks-hens) for cocks in range(100//5 +1 )
               for hens in range((100-cocks*5)//3 + 1)
               if 7 * cocks + 4 * hens == 100]
 
    print('总共有%d个解' % len(answer))
    for num,value in enumerate(answer,1):
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % (num, *value))
  
if __name__ == '__main__':
    cock_hen_chicken()
    print()
    cock_hen_chicken_all()
    

