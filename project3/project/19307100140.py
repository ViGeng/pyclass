#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util

def get_median(scores):
    size = len(scores)
    median=0.0
    if size % 2 == 0:
        median = (scores[size//2] + scores[size//2 - 1])/2
    if size % 2 == 1:
        median = scores[(size-1)//2]
    print('\n中位数%.1f' % (median))


if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)
    
    descending_scores = sorted(exam_scores, reverse = True)
    first_ten = descending_scores[0:10]
    print('\n前10位分数(从高到低)分别为')
    util.print_scores(first_ten)

    ascending_scores = sorted(exam_scores)
    last_ten = ascending_scores[0:10]
    print('\n后10位分数(从低到高)分别为')
    util.print_scores(last_ten)

    average = sum(exam_scores) / len(exam_scores)
    print('\n平均分%.1f' % (average))

    get_median(descending_scores)
