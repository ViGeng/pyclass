def main():
    e = 1
    i = 1
    item = 1
    while item < 10**10:
        item = item * i
        i += 1
        e = e + 1/item
    print('e =',e)
if __name__ == '__main__':
    main()
 
