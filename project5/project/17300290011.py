
def calculate_e(epsilon):
    e_Euler = 0
    value, res = 1, 1
    while 1/value >= epsilon: # 最后一项小于epsilon时停止
        e_Euler += 1 / value
        value *= res
        res += 1      
    print(e_Euler)

if __name__ == '__main__':
    epsilon = 10e-10
    calculate_e(epsilon)
