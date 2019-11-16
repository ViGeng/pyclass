if __name__ == '__main__':

    ##循环结构实现
    def chicken1(num,money):
        tmale = []
        tfemale = []
        tlittle = []
        for male in range(0, num // 5 + 1):
            for female in range(0, num // 3 + 1):
                if 5 * male + 3 * female + (num - male - female) / 3 == money:
                    tmale.append(male)
                    tfemale.append(female)
                    tlittle.append(num - male - female)
        
        print('总共有%d个解' %(len(tmale)))
        for i in range(0, len(tmale)):
            print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' %(i+1,tmale[i],tfemale[i],tlittle[i]))

    ##列表解析式实现
    def chicken2(num,money):
        tmale = [male for male in range(0, num // 5 + 1)
                 for female in range(0, num // 3 + 1)
                 if 5 * male + 3 * female + (num - male - female) / 3 == money]
        tfemale = [female for male in range(0, num // 5 + 1)
                 for female in range(0, num // 3 + 1)
                 if 5 * male + 3 * female + (num - male - female) / 3 == money]
        tlittle = [num - male - female for male in range(0, num // 5 + 1)
                 for female in range(0, num // 3 + 1)
                 if 5 * male + 3 * female + (num - male - female) / 3 == money]

        print('总共有%d个解' %(len(tmale)))
        for i in range(0, len(tmale)):
            print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' %(i+1,tmale[i],tfemale[i],tlittle[i]))


    chicken1(100,100)
    print()
    chicken2(100,100)
