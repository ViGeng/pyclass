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

exam_scores.sort(reverse = True)
top_10 = exam_scores[:10]
print('\n前%d位(从高到低)分别为: ' % len(top_10))
util.print_scores(top_10)

exam_scores.sort()
last_10 = exam_scores[:10]
print('\n后%d位(从低到高)分别为: ' % len(last_10))
util.print_scores(last_10)

average = sum(exam_scores) / len(exam_scores)
print('平均分为: %.1f' % average)

if len(exam_scores) % 2 == 0:
    mid_number1, mid_number2 = exam_scores[len(exam_scores)//2], exam_scores[len(exam_scores)//2+1]
    mid_number = (mid_number1 + mid_number2) / 2
    print('中位分为: %.1f' % mid_number)
else:
    mid_number = exam_scores[(len(exam_scores)+1)//2]
    print('中位分为: %.1f' % mid_number)
    
