def get_e():
    n=item=i=1
    e=1
    while i>=10**(-10):
        item*=n
        i=1/item
        e+=i
        n+=1
        i=1/item*n
    else:
        print('e =',e)

if __name__ == '__main__':
    get_e()
