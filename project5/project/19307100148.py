def main():
    total = 1
    i = item = 1

    while item <= 10**10 :
          item *= i 
          total += 1 / item
          i += 1

    print(' e=' ,total)


if __name__ == '__main__':
    main()
    
