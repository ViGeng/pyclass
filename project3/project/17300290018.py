#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util

def scores_sort(scores):
    scores.sort(reverse = True)
    print("\n前10位分数（从高到低）分别为")
    util.print_scores(scores[0:10])
    print("\n后10位分数（从低到高）分别为")
    util.print_scores(scores[-1:-11:-1])

def calculate_average(scores):
    S = sum(scores)
    N = len(scores)
    print("\n%s%.1f" % ("平均分", S/N))

def calculate_median(scores):
    N = len(scores)
    if N % 2 == 0:
        print("\n%s%.1f" % ("中位数", (scores[N // 2 - 1] + scores[N // 2]) / 2))
    else:
        print("\n%s%.1f" % ("中位数", scores[N // 2]))

if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

    scores_sort(exam_scores)
    calculate_average(exam_scores)
    calculate_median(exam_scores)

