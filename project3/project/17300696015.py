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



print() #空行


# 成绩排名前10名和后10名的学生分数
print('前10位分数（从高到低）分别为',sorted(exam_scores,reverse = True)[:10])
print('后10位分数（从低到高）分别为',sorted(exam_scores,reverse = False)[:10])


print() #空行



def mean(exam_scores):
    sum = 0
    for score in exam_scores:
        sum += score
        return sum/len(exam_scores)


def median(exam_scores):       
    exam_scores = sorted(exam_scores)      
    size = len(exam_scores)
    if size % 2 == 0:
        med = (exam_scores[size//2 - 1] + exam_scores[size//2])/2
    else:
        med = exam_scores[size//2]
    return med

n = exam_scores
m = mean(n)
print("平均分:{:.1f},中位数:{:.1f}.".format(m,median(n)))
