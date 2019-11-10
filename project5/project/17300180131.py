def calculate_e():
    place= 1
    sum_e = 1
    n=1
    minimum = int(input('请输入一个正整数，使得求和末项不小于10的负这个整数次幂'))

    while True:
        place *= (1/n)
        if place < (10**(-minimum)):
            break
        sum_e += place
        n = n+1

    print (sum_e)

if __name__ == '__main__':
    calculate_e()


