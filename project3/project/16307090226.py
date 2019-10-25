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
    sort_scores = sorted(exam_scores)
    top_10 = sort_scores[:-11:-1]
    top_10_from_highest_to_lowest = sorted(top_10,reverse = True)
    print('\n前10位分数（从高到低）分别为')
    util.print_scores(top_10_from_highest_to_lowest)
    print()
    worst_10 = sort_scores[:10]
    worst_10_from_lowest_to_highest = sorted(worst_10)
    print('\n后10位分数（从低到高）分别为')
    util.print_scores(worst_10_from_lowest_to_highest)
    print()
    average_exam_scores = sum(exam_scores[:])/len(exam_scores)
    print('平均分%.1f'%(average_exam_scores))
    print()
    if len(sort_scores) % 2 == 0:
        index_1 = (len(sort_scores)+1)//2
        index_2 = index_1 +1
        middle_score = (sort_scores[index_1]+ sort_scores[index_2])/2
    else:
        index_3 = (len(sort_scores)+1)//2
        middle_score = sort_scores[index_3]
    print('中位数%.1f'%(middle_score))
    

