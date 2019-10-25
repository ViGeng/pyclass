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

def main () :
    print (len (exam_scores))
    exam_scores.sort(reverse = True)
    print (" ")
    print ("前10位分数（从高到低）分别为" % (exam_scores))
    util.print_scores(exam_scores[:10])
    print (" ")

    exam_scores.sort()
    print ("后10位分数（从低到高）分别为" % (exam_scores))
    util.print_scores(exam_scores[:10])
    print (" ")

    a = sum(exam_scores[:]) / len(exam_scores)
    print ("平均分%.1f" %(a))

    b = len (exam_scores)
    if b % 2 == 0:
       m = (exam_scores[int(b/2) - 1] + exam_scores[int(b/2)]) / 2
       print (" ")
       print ("中位数%.1f" % m)
    else:
        m = exam_scores[int((b - 1) / 2)]
        print (" ")
        print ("中位数%.1f" % m)

main ()



