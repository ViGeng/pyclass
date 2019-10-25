#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util

def caculate_average(list_a):
    list_average = sum(list_a) / (len(list_a))
    return list_average

def caculate_middle(list_a):
    list_a_sorted = sorted(list_a)
    if len(list_a) % 2 == 0:
        middle_num = int(len(list_a) / 2)
        list_middle = list_a_sorted[int((list_a[middle_num] +
                                     list_a[middle_num - 1]) / 2)]
    else:
        middle_num = int((len(list_a) + 1) / 2)
        list_middle = list_a_sorted[middle_num - 1]
    return list_middle

if __name__ == '__main__':

    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)
    print()

    scores_sorted_1 = sorted(exam_scores,reverse = True)
    scores_sorted_1_10 = scores_sorted_1[:10]
    print('前10位同学的分数（从高到低）分别为：')
    util.print_scores(scores_sorted_1_10)
    print()
    
    scores_sorted_2 = sorted(exam_scores)
    scores_sorted_2_10 = scores_sorted_2[:10]
    print('后10位同学的分数（从高到低）分别为：')
    util.print_scores(scores_sorted_2_10)
    print()

    scores_average = caculate_average(exam_scores)
    print('平均分%.1f' % scores_average)
    print()

    scores_middle = caculate_middle(exam_scores)
    print('中位数%.1f' % scores_middle)
    

    

    

