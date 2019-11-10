def calculate_e(error):
    i = item = 1
    total = 1
    while 1 / item >= error:
        item *= i
        total += 1 / item
        i += 1
    return (i, total)

error = 1e-10
(steps, e) = calculate_e(error)
print('循环次数为：', steps, 'e值为：', e)