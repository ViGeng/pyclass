def main():
    i = 0
    e = 0
    t = 1
    while 1/t > 1e-10:
        e = e + 1/t
        i += 1
        t *= i
        print (e)

if __name__ == '__main__':
    main()
