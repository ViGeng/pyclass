

def main():
    c1_list=[]
    c2_list=[]

    for i in range(21):
        for j in range(int((100 - 5 * i) / 3) + 1):
            k = (100 - 5 * i - 3 * j) * 3
            if i + j + k ==100:
                c1_list.append((i,j,k))

    c2_list=[(i,j,k) for i in range(21) for j in range(int((100 - 5 * i) / 3) + 1)  for k in [(100 - 5 * i - 3 * j) * 3] if i + j + k ==100]


    if c1_list==c2_list:
        l = len(c1_list)
        print('共有%d个解'%l)
        for i in range(l):
            print('解%d:'%(i+1),end='')
            print('鸡翁 %d 鸡母 %d 鸡雏 %d '%c1_list[i])
    else:
        print('wrong')
            
    



if __name__=='__main__':
    main()
