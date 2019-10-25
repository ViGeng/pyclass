#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#Project3 作者：19级经济学院 应眺

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
    count = 0
    for score in exam_scores[-1:-11:-1]:
        print(score,end = '\t')
        count += 1
        if count % 5 == 0:
            print()
    print('\n后10位分数（从低到高）分别为')
    count = 0
    for score in exam_scores[:10]:
        print(score,end = '\t')
        count += 1
        if count % 5 == 0:
            print()

    average = sum(exam_scores)/len(exam_scores)
    print('\n平均分' + '%.1f'%average)

    if len(exam_scores) % 2 == 0:
        middle = (exam_scores[int(len(exam_scores)/2-1)] + \
                 exam_scores[int(len(exam_scores)/2)])/2
    else:
        middle = exam_scores[int((len(exam_scores)-1)/2)]
    print('\n中位数' + '%.1f'%middle)
