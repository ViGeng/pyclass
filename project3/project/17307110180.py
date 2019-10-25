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
    # 算前10
exam_scores = sorted(exam_scores, reverse = True)
exam_scores_slices = exam_scores[0:10]
print("前%d位分数(从高到低)分别为" % len(exam_scores))
count = 0
for exam_scores_slice in exam_scores_slices:
    print(exam_scores_slice, end = '\t')
    count += 1
    if count %5 == 0:
        print()
print()        

    #算后10
exam_scores_r = sorted(exam_scores)
exam_scores_r_slices = exam_scores_r[0:10]
print("后%d位分数(从低到高)分别为" % len(exam_scores_r))
count_r = 0
for exam_scores_r_slice in exam_scores_r_slices:
    print(exam_scores_r_slice, end = '\t')
    count += 1
    if count %5 == 0:
        print()
print()
    #算平均分
sum_grade = 0
for grade in exam_scores:
    sum_grade += grade
average_grade = sum_grade/len(exam_scores)
print("平均分" + str('%.1f' %average_grade))
print()
    #算中位数
long = (len(exam_scores))
if long %2 == 0:
    long = int(long/2)
    median = (exam_scores[long-1] + exam_scores[long])/2
if long %2 == 1:
    long = int((long-1)/2)
    median = exam_scores[long]
print("中位数" + str('%.1f' %median))



