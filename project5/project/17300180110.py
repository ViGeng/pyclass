def e(n):
    ''' 到某一项小于10**(-n)就不再求和 '''
    total=1
    i=item=1
    while item>=10**(-n):
        item/=i
        total+=item
        i+=1
    return total

print(e(10))
