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

    print()

exam_scores.sort(reverse=True)
first_ten=exam_scores[:10]
print('前10位分数（从高到低）分别为')
util.print_scores(first_ten)

print()

last_ten=sorted(exam_scores[-11:-1],reverse=False)
print('后10位分数（从低到高）分别为')
util.print_scores(last_ten)

print()

print('平均分','%.1f'%(sum(exam_scores)/len(exam_scores)),sep='')

print()

if len(exam_scores) % 2 == 0:
    print('中位数',(exam_scores[int(len(exam_scores)/2)] + exam_scores[int(len(exam_scores)/2+1)])/2,sep='')
else:
    print('中位数',exam_scores[int((len(exam_scores)+1)/2)],sep='')
    


