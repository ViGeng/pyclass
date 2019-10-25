#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util

list_a=project3_util.generate_exam_scores()

q=len(list_a)

print("总共%d同学成绩如下：" % q)
input(project3_util.generate_exam_scores()) 
list_1=sorted(list_a)

def main():
    list_2=list_1[0:9]
    list_b=list_1[::-1]
    list_3=list_b[0:9]
    print("前10位分数（从高到低）分别为）")
    print (list_3)

    
    print("后10位分数（从低到高）分别为")
    print (list_2)

    t=sum(list_a)
    average=t/q
    print("平均分%.1f" % average)

if __name__ == '__main__':
  main()




    





