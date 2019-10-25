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

    total = 0
    for i in range(len(exam_scores)):
        total += exam_scores[i]
    average = total / len(exam_scores)
    exam_scores.sort(reverse=True)
    if len(exam_scores) % 2 == 0:
        midian = (exam_scores[len(exam_scores) // 2] + exam_scores[len(exam_scores) // 2 -1]) / 2
    else:
        midian = exam_scores[len(exam_scores) // 2]

    ascending = exam_scores[:10]
    print('前十位分数（从高到低）分别为')
    util.print_scores(ascending)


    exam_scores.sort()
    descending = exam_scores[:10]
    print('后十位分数（从低到高）分别为')
    util.print_scores(descending)

    print('平均分%.1f' % average)
    print('中位数%.1f' % midian)
    input()



