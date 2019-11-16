for i in range(0,100):
        for j in range(0,100):
            for k in range(0,100):
                if ((i+j+k)==100 and (5*i+3*j+k/3)==100):
                    print(" 鸡翁的数量是 %d 鸡母的数量是 %d 鸡雏的数量是 %d" % (i, j, k))
