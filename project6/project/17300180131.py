def circle_solution():
    solution=list()
    for cocks in range(15):
        hens = 25 - (7*cocks)/4
        if hens%1 == 0:
            hens = int(hens)
            chicken = 3*(100-5*cocks-3*hens)
            solution.append([cocks,hens,chicken])
    
    for item in solution:
        print('鸡翁 %s 鸡母 %s 鸡雏 %s'%(item[0],item[1],item[2]))

def list_solution():
    alist = [(x,25-7*x/4,300-15*x-9*(25-7*x/4)) for x in range(15) if (25-7*x/4)%1 == 0]
    for item in alist:
        print('鸡翁 %s 鸡母 %.f 鸡雏 %.f'%(item[0],item[1],item[2]))
        
if __name__ == "__main__":
    print('循环结构解法结果：')
    circle_solution()
    print('')
    print('列表解析式解法结果：')
    list_solution()
    
   
    
