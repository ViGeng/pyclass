#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util


if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

    # 你编写的代码放在后面

    #前十位后十位排序
    exam_scores.sort()
    highest_10 = []
    lowest_10 = []

    for i in range(10):
        highest_10.append(exam_scores[-i-1])
        lowest_10.append(exam_scores[i])

    print('\n前10位分数(从高到低)分别为')
    util.print_scores(highest_10)
    print('\n后10位分数(从低到高)分别为')
    util.print_scores(lowest_10)

    #平均分
    average = sum(exam_scores) / len(exam_scores)
    print('\n平均分%.1f' % average)

    #中位数
    num = len(exam_scores)
    if num % 2 == 0:
        median = (exam_scores[int((num / 2) - 1)] + exam_scores[int(num / 2)]) / 2
    else:
        median = exam_scores[int((num - 1) / 2)]
    print('\n中位数%.1f' % median)

