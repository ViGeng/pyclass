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
    
exam_scores.sort(reverse = True)

alist = exam_scores[:10]
print('\n前十位分数（从高到低）分别为')
util.print_scores(alist)

blist = exam_scores[-1:-11:-1]
print('\n后十位分数（从高到低）分别为')
util.print_scores(blist)

total = sum(exam_scores)
cal = len(exam_scores)
x = total / cal

print('\n平均分%.1f'%x)

def median(exam_scores):
    if cal % 2 == 1:
        m = int(cal / 2) + 1
        n = exam_scores[m-1]
    else:
        m = int(cal / 2)
        j = exam_scores[m-1]
        k = exam_scores[m]
        n = (j + k) / 2
    return n

r = median(exam_scores)
print('\n中位数%.1f'%r)
