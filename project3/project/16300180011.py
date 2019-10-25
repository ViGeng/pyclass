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

   
    exam_scores.sort(reverse=True)
    top10 = exam_scores[:10]
    last10 = exam_scores[-1:-11:-1]

    print()
    print('前10位分数(从高到低)分别为')
    util.print_scores(top10)
    print()
    print('后10位分数(从低到高)分别为')
    util.print_scores(last10)

    n = len(exam_scores)
    S = sum(exam_scores)
    average = S / n #平均数
    if n % 2:
        mean = exam_scores[int(((n - 1) / 2))]   #奇时中位数
    else:
        mean = (exam_scores[int(n / 2)] + exam_scores[int(n / 2) - 1]) / 2   #偶时中位数

    print()
    print('平均分%.1f'% average)
    print()
    print('中位数%.1f'% mean)

