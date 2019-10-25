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
    alist = exam_scores
    alist.sort()

    print('前10位分数(从高到低)分别为')
    blist = alist[-1:-10:-1]
    blist = [str(i) for i in blist]

    count = 0
    for i in blist:
        print(i, end='\t')
        count += 1
        if count % 5 == 0:
            print()
    if count % 5 != 0:
        print()
        
    print()
    print('后10位分数(从低到高)分别为')
    clist = alist[:10]
    clist = [str(e) for e in clist]

    count = 0
    for e in clist:
        print(e, end='\t')
        count += 1
        if count % 5 == 0:
            print()
    if count % 5 != 0:
        print()

    print()
    t = sum(alist) / len(exam_scores)
    print('平均分', '%.1f' % t)

    print()
    if (len(exam_scores) % 2)== 1:
        x = len(exam_scores) // 2
        y = alist[x]
        print('中位数', y)
    else:
        y = (alist[len(exam_scores)//2] + alist[len(exam_scores)//2 - 1])/2
        print('中位数', y)
