e = 0
time = 0
single = 1

while single > 1e-10:
    e += single
    time += 1
    single /= time
    print(e)

print("\n欧拉数e的值是" + str(e))
