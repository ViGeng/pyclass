def solution():
    solution = []
    count_item = 0
    for a in range(0,100):
        for b in range(0,100):
            for c in range(0,100):
                if 5*a + 3*b + 1/3*c == 100 and a + b + c ==100:
                    count_item += 1
                    solution.append(a)
                    solution.append(b)
                    solution.append(c)
    print('总共有%d个解'%count_item)
    for i in range(0,count_item):
        print('解%d:鸡翁%3d 鸡母%3d 鸡雏%3d'%(i,solution[3*i],solution[3*i+1],solution[3*i+2]))

solution()

def find_k():
    result=[(x,y,z) for x in range (100) for y in range (100) \
            for z in range (100) if x+y+z==100 and 5*x+3*y+z/3==100]
    print(result)
find_k()
