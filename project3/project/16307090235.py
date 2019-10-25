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
    # sort1 = 前十位分数（从高到低）分别是：
    # sort2 = 后十位分数（从低到高）分别是：
    # sort_average = 平均分是：
    # sort_middle = 中位数是：

    print()
    print()

    sort_scores = sorted(exam_scores)
    sort1 = sort_scores[-1:-11:-1]
    sort1 = sorted(sort1,reverse = True)
    print('前十位分数(从高到低)分别是：')
    util.print_scores(sort1)
    print()
    print()
    sort2 = sort_scores[0:10]
    sort2 = sorted(sort2)
    print('后十位分数(从低到高)分别是：')
    util.print_scores(sort2)
    print()
    print()
    sort_average = sum(exam_scores[:])/len(exam_scores)
    print('平均分是：%.1f' %(sort_average))
    print()
    print()
    if len(sort_scores) % 2 != 0:
        index1 = (len(sort_scores)+1)//2
        sort_middle = sort_scores[index1]
    else:
        index2 = (len(sort_scores)+1)//2
        index3 = index2 +1
        sort_middle = (sort_scores[index2] + sort_scores[index3])/2
    print('中位数是：%.1f'%(sort_middle))
    
        

    


    
