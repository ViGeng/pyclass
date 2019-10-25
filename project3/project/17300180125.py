#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import sys
sys.path.append('D:\\University\\课件\\Python程序设计')
#需要引用的模块放在这个路径里面

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
    import math
    def average_score(exam_scores):
        sumscore=sum(exam_scores)
        average_score=sumscore/len(exam_scores)
        return average_score

    def medium_score(another_exam_scores):
        if len(another_exam_scores)%2 == 1:
           i=int((len(another_exam_scores)+1)/2)
           medium_score=int(another_exam_scores[i])
           return medium_score
        else:
           i=int(len(another_exam_scores)/2)
           medium_score=(int(another_exam_scores[i])+int(another_exam_scores[i+1]))/2

        return medium_score

    print()
    new_exam_scores=sorted(exam_scores,reverse=True)
    a_list=new_exam_scores[0:10] 
    another_exam_scores=sorted(exam_scores)
    b_list=another_exam_scores[0:10]
    print("前10位分数（从高到低）分别为")
    util.print_scores(a_list)
    print()
    print("后10位分数（从低到高）分别为")
    util.print_scores(b_list)
    print()
    average_score='%.1f'%average_score(exam_scores)
    print("平均分",average_score)
    print()
    medium_score='%.1f'%medium_score(another_exam_scores)
    print("中位数",medium_score)
       
    
