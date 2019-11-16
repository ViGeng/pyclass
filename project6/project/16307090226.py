#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


def hundreds_chicken_puzzle_solution1(numbers=100, money=100):
    found = False
    answer = 1
    answer_list = []
    for elder_chicken in range (0, numbers+1):
        for hen in range (numbers+1):
            chicken = numbers - elder_chicken - hen
            if ((chicken + elder_chicken + hen == numbers) and (5*elder_chicken + 3*hen + chicken/3 == 100)):
                answer += 1
                answer_list_append = answer_list.append([elder_chicken, hen, chicken])
                
                found = True
                
                
    if not found:
        print('无解')
    
    print('总共有%d个解' % (answer-1))   
    for i in range(1,answer):
        print('解%d: 鸡翁 %d 鸡母 %d 鸡雏 %d' % (i,(answer_list[i-1][0]),(answer_list[i-1][1]),(answer_list[i-1][2])))
                

def hundreds_chicken_puzzle_solution2(numbers=100, money=100):
    answer_list = [(i,hen,numbers-i-hen) for i in range (0, numbers+1)
                   for hen in range (numbers+1)if(5*i + 3*hen + (numbers-i-hen)/3 == 100)]
    answer_list_append = answer_list.append([])

    print('总共有%d个解' % (len(answer_list)-1))   
    for i in range(1,len(answer_list)):
        print('解%d: 鸡翁 %d 鸡母 %d 鸡雏 %d' % (i,(answer_list[i-1][0]),(answer_list[i-1][1]),(answer_list[i-1][2])))
    

                
                


if __name__ == '__main__':
    hundreds_chicken_puzzle_solution1()
    print('-'*30)
    hundreds_chicken_puzzle_solution2()
    

