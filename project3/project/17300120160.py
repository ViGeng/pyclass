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

    
    exam_scores.sort(reverse=True)
    high=exam_scores[0:10]
    low=exam_scores[-10:]
    print("前10位分数（从高到低）分别为")
    print(high)
    print("前10位分数（从低到高）分别为")
    print(low)
    sum=sum(exam_scores)
    average=float(sum/len(exam_scores))
    print('平均分为'+'%.2f'%average)

