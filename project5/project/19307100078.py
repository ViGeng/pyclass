def value():
    x = e = 1
    
    i = 1
    while x <= 10**10:
        x *= i
        e += 1/x
        i += 1
    print ("e =",e)

if __name__=="__main__":           
    value()
