# coding = 'utf-8'
if __name__ == '__main__':
    minimization = 10**(-10)
    i=1
    start = 1
    euler_number = 0
    while(True):
        item = 1 / start
        euler_number += item
        if item <= minimization:
            break
        else:
            start *= i
            i = i + 1

    print('e =',euler_number)
        
        
