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
    exam_scores.sort()
    high=exam_scores[-10:]
    low=exam_scores[0:10]
    high.sort(reverse=True)
    num=len(exam_scores)
    aver=sum(exam_scores)/num
    print()
    print('前10位分数（从高到低）分别为')
    util.print_scores(high)
    print()
    print('后10位分数（从低到高）分别为')
    util.print_scores(low)
    print()
    print('平均分%.1f'% aver)
    print()
    if num%2==1:
        median=exam_scores[int((num-1)/2)]
    if num%2==0:
        median=exam_scores[int(num/2)]+exam_scores[int((num-2)/2)]
        median=median/2
    print('中位数%.1f'% median)
