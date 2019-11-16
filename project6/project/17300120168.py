def chickennumber(chicken = 100, money = 100):
    i = 0
    aList = []
    for father in range(0, chicken+1):
        for mother in range(0, chicken+1):
            if 5 * father + 3 * mother + (chicken-mother-father)/ 3 == money:
                i += 1
                result = (i, father, mother, chicken-father-mother)
                aList.append(result)                          
    print('总共有%d个解' % len(aList))
    for item in aList:
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % (item[0],item[1],item[2],item[3]))


def chickennumbers (chicken = 100, money = 100):
    result = [ (father, mother, chicken-father-mother) for father in range(0, chicken+1) for mother in range(0, chicken+1)
                   if 5 * father + 3 * mother + (chicken-mother-father)/ 3 == money]
    print('总共有%d个解' % len(result))
    for item in result:
        print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % (result.index(item)+1,item[0],item[1],item[2]))
               
                   

if __name__ == '__main__':
    chickennumber(chicken = 100, money = 100)
    print()
    chickennumbers(chicken = 100, money = 100)
