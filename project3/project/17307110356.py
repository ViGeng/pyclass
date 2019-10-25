#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import project3_util as util                                                     #可以直接调用该py里的变量名？
                                                                                 #如是，为什么还会显示 name 'scores' is not defined ？

if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

    # 你编写的代码放在后面

    ordered_scores = sorted(exam_scores)                                         #list.sort()  list用已定义的列表名称替代！
                #用内置sorted()可将排序后结果存储下来，.sort只能返回none

    last_10 = ordered_scores[0:10]
    first_10 = ordered_scores[-1:-11:-1]                                         #切片注意[起始下标:终止下标:间隔！！！]

    average = sum(exam_scores) / len(exam_scores)

    print('\n前10位分数（从高到低）分别为')
    util.print_scores(first_10)
    print('\n后10位分数（从低到高）分别为')
    util.print_scores(last_10)

    print('\n平均分', "%.1f" %average)

    l = len(exam_scores)
    if l % 2 == 0:
        middle =  (ordered_scores[int(l / 2 - 1)] + ordered_scores[int(l / 2)]) / 2
        print('\n中位数', "%.1f" %middle)
    else:
        middle = ordered_scores[int((l - 1) / 2)]
        print('\n中位数', middle)



