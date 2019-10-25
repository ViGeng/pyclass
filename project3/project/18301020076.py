#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util

def get_median():                                   #定义函数求中位数
    exam_scores = util.generate_exam_scores()
    exam_scores.sort()
    half = len(exam_scores)//2
    median = (exam_scores[half] + exam_scores[~half]) / 2
    return median

if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

    # 以下为我编写的代码
    
    print()
    print("前10位分数(从高到低）分别为")            #前10的分数
    exam_scores.sort(reverse = True)
    util.print_scores(exam_scores[:10])
    
    print()
    print("后10位分数（从低到高）分别为")            #后10的分数
    exam_scores.sort()
    util.print_scores(exam_scores[:10])

    average = sum(exam_scores)/len(exam_scores)      #计算平均分
    print()
    print("平均分%.1f" % average)

    median = get_median()                            #计算中位数
    print()
    print("中位数%.1f" % median)

