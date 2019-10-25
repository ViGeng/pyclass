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

print()

exam_scores.sort(reverse = True)
alist = exam_scores[:10]
print("前10位分数(从高到低)分别为")
util.print_scores(alist)

print()

exam_scores.sort()
blist = exam_scores[:10]
print("后10位分数(从低到高)分别为")
util.print_scores(blist)

print()

j = 0
for i in exam_scores:
    j += i
p = j / len(exam_scores)

print("平均分%.1f"%p)

print()

if len(exam_scores) % 2 == 0:
    m = exam_scores[int(len(exam_scores)/2-1)]
    n = exam_scores[int(len(exam_scores)/2)]
    k = (m + n) / 2
else:
    k = exam_scores[int((len(exam_scores)-1)/2)]
print("中位数%.1f"%k)
