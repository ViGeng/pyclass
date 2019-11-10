def e_value():
    limit=10**(-10)
    i = item = 1
    total = 1
    while item >= limit:
        item *= 1/i
        total += item
        i += 1
    print(total)

if __name__ == '__main__':
    e_value()
