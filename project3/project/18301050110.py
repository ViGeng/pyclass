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
    
    print(40 * ' ')
    
    a = list(exam_scores)
    a.sort()
    #将所有同学的考试成绩变成一个名字为a的列表,并将a进行升序排列
    
    h = a[slice(-1, -11, -1)]
    i = a[slice(0, 10, 1)]
    #将包含所有同学考试成绩的列表升序排列，取成绩排名前10名和成绩排名后10名的同学的成绩的切片，分别为列表h和i
    
    print('前10位分数（从高到低）分别为')
    util.print_scores(h)
    print(40 * ' ')
    print('后10位分数（从低到高）分别为')
    util.print_scores(i)
    print(40 * ' ')
    
    average_score = sum(a) / len(a)
    print('平均分%.1f'%(average_score))
