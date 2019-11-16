#法1
i = 0
print('总共有4个解')
for chicks in range(0, 101):
    for hens in range(0, 101):
        for cocks in range(0, 101):
            if cocks * 5 + hens * 3 + chicks / 3 == 100 and cocks + hens + chicks == 100:
                i += 1
                print('解%.0f:鸡翁'%i, cocks,'鸡母', hens,'鸡雏', chicks)

print()

#法2
result = [(x, y, 100 - x - y) for x in range(0, 101) for y in range(0, 101)
          if x * 5 + y * 3 + (100 - x - y) / 3 ==100]
print('总共有4个解')
print('解1:鸡翁', result[0][0], '鸡母', result[0][1], '鸡雏', result[0][2])
print('解2:鸡翁', result[1][0], '鸡母', result[1][1], '鸡雏', result[1][2])
print('解3:鸡翁', result[2][0], '鸡母', result[2][1], '鸡雏', result[2][2])
print('解4:鸡翁', result[3][0], '鸡母', result[3][1], '鸡雏', result[3][2])

