#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util

def main():
    exam_scores.sort() #升序
#    util.print_scores(exam_scores)
    min_10=exam_scores[:10]
    l=len(exam_scores)
    max_10=exam_scores[l-10:l]
    max_10.reverse()
    s=0
    for x in exam_scores:
        s=s+x
    average = float(s)/l
    if l%2==0:
        median = (float(exam_scores[l//2-1])+float(exam_scores[l//2]))/2
    else:
        median = exam_scores[l//2]
    print('\n前10位分数（从高到低）分别为')
    util.print_scores(max_10)
    print('\n后10位分数（从低到高）分别为')
    util.print_scores(min_10)
    print('\n平均分%.1f' % average)
    print('\n中位数%.1f' % median)

if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

    # 你编写的代码放在后面
    main()
    
