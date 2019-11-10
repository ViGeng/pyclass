def main():
    item = 1
    i = 2
    total = 1
    while item <= 10**10:
        total = total + 1/item
        item = item * i 
        i = i+1  
    print("自然对数的底数e的值为%.10f" %total)

if __name__=="__main__":
    main()
