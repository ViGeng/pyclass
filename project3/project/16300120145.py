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
new_s = exam_scores[0:10]
print('\n前%d位分数（从高到低）分别为:' % len(new_s))
util.print_scores(new_s)

exam_scores.sort()
new_s1 = exam_scores[-10:]
print('\n后%d位分数（从低到高）分别为:'% len(new_s1))
util.print_scores(new_s1)

average = float(sum(exam_scores)/len(exam_scores))
print('\n平均分%.1f'% average)

l = len(exam_scores)
exam_scores.sort()
m1,m2 = exam_scores[l//2],exam_scores[l//2+1]
if l%2 == 0:
    m = (m1+m2)/2
    print ('\n中位数%.1f'% m)
else:
    m = m2
    print ('\n中位数%.1f'% m)
    

