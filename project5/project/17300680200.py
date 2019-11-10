if __name__ == '__main__':
    (i,euler,e) = (1,1,1)
    while 1 / euler >= 10 * 10**(-10):
        euler = euler * i
        e = e + 1 / euler
        i = i + 1
    print('%3s %.20f'%('e =',e))
