i = item = 1
total = 1
while item > 10**-20:
    item *= 1/i
    total += item
    i += 1
print(total)

