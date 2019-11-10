if __name__ == '__main__':
    e = 1
    a = 1
    i = 1
    while a >= 10**-10:
        s = 1
        for j in range (1,i+1):
            s=s*j
        a = 1/s
        e = e + a
        i +=1
    print(e)
    
