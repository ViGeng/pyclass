#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util

def top_ten_scores(exam_scores):  
    top_ten = exam_scores[0:10]
    print('\n前十位分数（从高到低）分别为\n' )
    util.print_scores(top_ten)

def end_ten_scores(exam_scores):  
    end_ten = exam_scores[-1:-11:-1]
    print('\n后十位分数（从低到高）分别为\n' )
    util.print_scores(end_ten)

def average_scores(exam_scores):
    Sum = sum(exam_scores)
    average_scores = float(Sum/len(exam_scores))
    print('\n平均分%.1f' % average_scores)

def median_scores(exam_scores):
    N = len(exam_scores)
    if N % 2 == 0:
        print('\n中位数%.1f' % ((exam_scores[N // 2 - 1] + exam_scores[N // 2]) / 2))
    else:
        print('\n中位数%.1f' % (exam_scores[N//2]))


if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)
 
    exam_scores.sort(reverse = True)

    top_ten_scores(exam_scores)
    end_ten_scores(exam_scores)
    average_scores(exam_scores)
    median_scores(exam_scores)


        
    

    
    


    
