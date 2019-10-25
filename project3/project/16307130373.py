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
     
    exam_scores.sort()#将成绩排序
    #print(exam_scores)
    high_grade = exam_scores[-1:-11:-1]  #得到前10个分分
    low_grade = exam_scores[:10:1] #得到倒数10个分数
    
    print('\n前10位分数（从高到低）分别为')
    util.print_scores(high_grade)

    print('\n后10位分数（从低到高）分别为')
    util.print_scores(low_grade)

    sum_grade = 0
    for i in exam_scores:
        sum_grade += i
    average_score = sum_grade / float(len(exam_scores))
    print('\n平均分%.1f'%average_score)


    if (len(exam_scores) % 2) == 1:
        median = exam_scores[int((len(exam_scores) - 1) / 2)]
    else:
        median = (exam_scores[int((len(exam_scores) - 2) / 2)] + exam_scores[int(len(exam_scores) / 2)] )/ 2
    print('\n中位数%.1f'%median)
        
       
    

   

