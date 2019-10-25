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


    exam_scores.sort()
    last_ten=exam_scores[0:10]
    ahead_ten=exam_scores[-1:-11:-1]
    print('前10位分数（从高到低）分别为')
    util.print_scores(ahead_ten)
    print('后10位分数（从低到高）分别为')
    util.print_scores(last_ten)
    a=sum(exam_scores)/len(exam_scores)
    print('平均分%.1f' % a)
    if len(exam_scores)%2==1:
        b=(len(exam_scores)-1)//2
        c=exam_scores[b]
        print('中位数%.1f' % c)
    else :
        b_1=(len(exam_scores)//2)-1
        b_2=b_1+1
        c_1=exam_scores[b_1]
        c_2=exam_scores[b_2]
        c=(c_1+c_2)/2
        print('中位数%.1f' % c)
    
    
