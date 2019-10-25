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
    first10 = exam_scores[-1:-11:-1]
    last10 = exam_scores[0:10]
    print()
    print('前10位分数（从高到低）分别为')
    util.print_scores(first10)
    print()
    print('后10位分数（从低到高）分别为')
    util.print_scores(last10)

    average = sum(exam_scores)/len(exam_scores)
    print()
    print('%3s%4.1f'%('平均分',average))

    middle1 = int((len(exam_scores) // 2))
    middle2 = -middle1
    middle3 = middle2 - 1
    middle_score = (exam_scores[middle1] + exam_scores[middle3]) / 2
    print('%3s%4.1f'%('中位数',middle_score))
    
