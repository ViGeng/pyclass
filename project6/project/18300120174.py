def method1():
    a = []
    result = 0
    for g in range(0, 21):
        for m in range(0, 34):
            for c in range(0, 301):
                if g+m+c == 100 and 5*g+3*m+c/3 == 100:
                    result = result + 1
                    a.append((result, g, m, c))
    print("总共有%d个解" % result)
    for i in range(result):
        print("解%d: 鸡翁 %d 鸡母 %d 鸡雏 %d" % a[i])

def method2():
    a = [(g, m, c) for g in range (0, 21)
         for m in range(0, 34)
         for c in range(0, 301)
         if g+m+c == 100 and 5*g+3*m+c/3 == 100]
    print("总共有%d个解" % len(a))
    for i in range (len(a)):
        print("解%d: 鸡翁 %d 鸡母 %d 鸡雏 %d" % (i+1, *a[i]))
    
    
if __name__ == '__main__':
    method1()
    method2()