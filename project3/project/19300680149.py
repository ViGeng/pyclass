#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import project3_util as util


def average():
    sumscore=0
    for item in scores:
        sumscore=sumscore+item
    number = len(scores)
    averagescore = sumscore/number
    print('平均数：%.1f' % averagescore)
    moderate()

def moderate():
    number = len(scores)
    if number % 2 == 0:
        moderatescore = 0.5* (scores[number//2]+scores[(number//2)+1])
    else:
        moderatescore = scores[(number+1)//2]#真除法返回的是浮点数
    print('中位数：%.1f' % moderatescore)

    
if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

    # 你编写的代码放在后面
    scores=util.generate_exam_scores()
    scores.sort()
    thefirst = scores[-1:-11:-1]   
    print('前10位分数（从高到低）分别为：')
    util.print_scores(thefirst)
    thelast = scores[:10]
    print('后10位分数（从低到高）分别为：')
    util.print_scores(thelast)

    average()






