
def cook_hen_chick_expense(quantity=100,expense=100):
    found = False
    for cook in range(0,101):
        for hen in range(0,101):
            chick = 100-cook-hen
            if (chick % 3 == 0) and (5*cook+3*hen+1*chick//3 == 100):
                print("鸡翁",cook,"鸡母",hen,"鸡雏",chick)
                found = True
                break
    if not found:
        print("无解")
 
        
 
#用列表推导式
def cook_hen_chick_expense2(quantity=100,expense=100):
    result = [[cook,hen,100-cook-hen]for cook in range(0,101)for hen in range(0,101)
            if (100-cook-hen) % 3 ==0 and cook*5 + hen*3 + 1*(100-cook-hen)//3== 100]

    if (result == ''):
        print('无解')
              
    else:
        print(result)
        print(" " * 40) 

        list1 = result
    
        for i in list1:
            print(i)
        print('')

    


        
if __name__ == '__main__':
    cook_hen_chick_expense()
    print(" " * 40)  


if __name__ == '__main__':
    cook_hen_chick_expense2()
    print(" " * 40)  











