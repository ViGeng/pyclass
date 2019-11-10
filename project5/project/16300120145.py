
def sum_e():
    #sum_e = 1 + 1 + 1/2 + 1/6 +1/24...
    i = n = 1
    item = 1
    e = 1

    while i >= 10**(-10):
        item *= n
        i = 1/item 
        e += i
        n += 1
        i *= 1/n
       
    else:
        print("e =",e)

if __name__ == '__main__':
    sum_e()
