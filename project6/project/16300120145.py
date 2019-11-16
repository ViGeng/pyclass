
def daddy_mommy_baby(chicken = 100, mon_chicken = 100):
    #公鸡5钱，母鸡3钱，1个小鸡1/3钱，100钱买100鸡
    found = False
    result = []
    for daddy in range(0, chicken+1):
        for mommy in range(chicken+1):
            for baby in range(chicken+1):
                if((daddy + mommy + baby) == chicken
                   and (5 * daddy + 3 * mommy + 1/3 * baby) == mon_chicken):
                    key = (daddy, mommy, baby)
                    result.append(key)
                    found = True
                    break

    print('总共有%d个解'% len(result))
    for i in result:
        print('解%d:鸡翁%d,鸡母%d,鸡雏%d'%((result.index(i)+1),*i))

    if not found:
        print ('无解')

def daddy_mommy_baby1():
    result = [(daddy,mommy,baby) for daddy in range(101) for mommy in range(101) for baby in range(101)
              if daddy + mommy + baby == 100 and 5 * daddy + 3 * mommy + baby * 1/3 == 100]

    print('\n总共有%d个解'% len(result))
    for i in result:
        print('解%d:鸡翁%d,鸡母%d,鸡雏%d'%((result.index(i)+1),*i))
              
if __name__ == '__main__':
    daddy_mommy_baby(chicken = 100, mon_chicken = 100)
    daddy_mommy_baby1()
    
