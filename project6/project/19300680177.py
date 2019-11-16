#method 1
def chicken(headers=100, money=100):
    print("总共有4个解")
    i = 0
    for males in range(0, headers+1):
        for females in range(headers+1):
            if ((males * 5 + females * 3 + (headers - males - females)/3) == money
                and (males + females + (headers - males - females)) == headers):
                i = i + 1
                print("解%d:鸡翁"%i,males, "鸡母", females, "鸡雏",(headers- males - females))

if __name__ == '__main__':
    chicken()
 


#method 2
s = [(x, y, z) for x  in range(101) for y in range(101) for z in range(101)
    if x * 5 + y * 3 + z / 3 == 100 and x + y + z == 100]

l = len(s)
print("总共有%d个解"%l)
for i in range(1, l + 1):
    print("解%d:鸡翁"%i,s[i - 1][0], "鸡母", s[i - 1][1], "鸡雏", s[i - 1][2])


 
