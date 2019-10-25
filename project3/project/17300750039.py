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
    exam_scores.sort()
    print('\n前10位分数（从高到低）分别为')
    util.print_scores(exam_scores[-1:-11:-1])
    print('\n后10位分数（从低到高）分别为')
    util.print_scores(exam_scores[:10])
    
    sumscore = 0
    for score in exam_scores:
        sumscore += score
    print('\n平均分%.1f' % (sumscore/len(exam_scores)))

    middlescore = 0
    if len(exam_scores) % 2 == 0:
        middlescore = (exam_scores[len(exam_scores) // 2] + exam_scores[len(exam_scores) // 2 - 1]) / 2
    else:
        middlescore = (exam_scores[len(exam_scores) // 2])
    print('\n中位数%.1f' % middlescore)
