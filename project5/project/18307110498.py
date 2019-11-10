def main():
    
    i = 0
    e = 1
    t = 1

    while t <= 10**(10):
       
       i = i + 1
       t = t * i
       e = e + 1/t
       
       print(e)

if __name__ == '__main__':

    main()

