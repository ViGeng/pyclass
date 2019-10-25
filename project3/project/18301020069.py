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

    for i in range(len(exam_scores)):  
        for j in range(len(exam_scores) - i - 1):  
            if exam_scores[j + 1] >= exam_scores[j]:  
                exam_scores[j], exam_scores[j + 1] = exam_scores[j + 1], exam_scores[j]
    
    print("前十名学生的成绩：\t")
    print(exam_scores[0:10])
    print("后十名学生的成绩：\t")
    print(exam_scores[-11:-1])
    print("学生平均成绩：\t")
    print(round(sum(exam_scores)/len(exam_scores),1))



