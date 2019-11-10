def Euler_number():
    i = 1
    a = 1
    e = 1
    while a<100000000000000000:
        e = 1/(a)+ e
        i = i + 1
        a = a * i
    else:
        print(e)
        
Euler_number()

        
        
