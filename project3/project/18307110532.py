#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util


if __name__ == '__main__':
   
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

    x=list(exam_scores)
    x.sort()
    x.reverse()
    aList=x
    y=aList[:10]
    print('\n前10位分数（从高到低）分别为')
    util.print_scores(y)
    x.reverse()
    aList=x
    z=aList[:10]
    print('\n后10位分数（从低到高）分别为')
    util.print_scores(z)
    n=len(exam_scores)
    a=sum(x)/n
    print()
    print('平均分',"%.1f"%a)

    

