def main():
    i = 0
    e = 0
    t = 1
    s = 1 / t
    while (s >= 10**(-10)):
        e = e + s
        i += 1
        t = t * i
        s = 1 / t
    e = e + s
    return e

if __name__ == '__main__':
    e = main()
    print('e=',e)

