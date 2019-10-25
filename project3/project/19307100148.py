#! /usr/bin/env python3
#  -*- coding: utf-8 -*-


import random

def print_scores(scores):
    """ 打印scores中的分数，每行5个数值"""
    count = 0
    for score in scores: 
        print(score, end='\t')
        count += 1
        if count % 5 == 0:
            print() 
    if count % 5 != 0:
        print() 


def generate_exam_scores():
    """ 某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    total = random.randint(45, 90)
    scores = []
    for i in range(total):
        scores.append(random.randint(50, 100))
    return scores

if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores =generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    print_scores(exam_scores)

    # 你编写的代码放在后面
    exam_scores.sort(reverse = True)

    c = round(sum(exam_scores) / (len(exam_scores)),1)

    print('前10位分数(从高到低)分别为')
    print_scores(exam_scores[0:9])
    
    print('后10位分数(从高到低)分别为' )
    print_scores(exam_scores[-10:-1])
    
    print('平均分', str(c) )
    


    
