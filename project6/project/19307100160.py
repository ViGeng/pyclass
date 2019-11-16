def hundred_chicken1():
    result1 = []
    for weng in range(21):
        for mu in range(34):
            for chu in range(300):
                if (5*weng + 3*mu + chu/3 == 100) and (weng + mu + chu == 100):
                    result1.append((weng,mu,chu))
    print('总共有4个解')
    for i,n in enumerate(result1):
        print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d'%(i+1,n[0],n[1],n[2]))
    
def hundred_chicken2():
    result2 = [(i,j,k) for i in range(21) for j in range(34) for k in range(300)
              if ((5*i + 3*j + k/3 == 100) and (j + k + i == 100))]
    print('总共有4个解')
    for i,n in enumerate(result2):
        print('解%d：鸡翁 %d 鸡母 %d 鸡雏 %d'%(i+1,n[0],n[1],n[2]))

if __name__ == '__main__':
    hundred_chicken1()
    hundred_chicken2()
    


    
