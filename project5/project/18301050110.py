#计算自然对数的底数 e  的值

def Euler_number(n):
    i = 1
    total = 1
    item = 1
    while item >= n:
        item *= 1 / i
        total += item
        i += 1

    return total

n = 10 ** (-10)
print(Euler_number(n))
