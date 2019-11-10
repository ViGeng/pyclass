def main():
    b = 1
    a = 1
    i = 1
    while a >= 10 ** (-10):
        b = b + a
        a = a / (i + 1)
        i = i + 1
    print('%s%f'% ('e = ', b))

if __name__ == '__main__':
    main()
