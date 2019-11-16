#列表解析法
headers,cost = 100,100

result = [ (i,j,headers - i - j)
           for i in range(0,headers)
           for j in range(headers+1)
             if 5 * i + 3 * j +1/3 * (headers-i-j) == cost ]
print('总共有%d个解' % (len(result)))
print(*result)

#循环结构
def main (headers = 100,cost = 100):
    count = 0
    found = False
    for cocks in range(0,headers+1):
        for hens in range(headers):
            if (( 5 * cocks + 3 * hens +1/3 * (headers-hens-cocks) == cost)):
                count += 1
                print ('鸡翁%d 鸡母%d 鸡雏%d' % (cocks,hens,headers-cocks-hens))
                found = True
                break
    print ('总共有%d个解' % (count))
    
    if not found:
        print('无解')


        
            
if __name__ == '__main__':
    main()


