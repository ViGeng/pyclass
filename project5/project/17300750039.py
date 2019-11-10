if __name__ == '__main__':
    i = item = 1
    sum = 1.0
    while True:
        item *= i
        sum += 1 / item
        if (1 / item < 10 ** (-10)):
            break
        i += 1

    print('e的值为',sum)
