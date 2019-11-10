
def sum_factorial1():
    i = 1
    item = 1.0#浮点数(但好像直接写1也可以？）
    e = 1.0

    while item < 10**10:
        item *= i
        e += 1.0/item
        i += 1
    return e


if __name__ == '__main__':
    e = sum_factorial1()
    
    print('e = ', e)
