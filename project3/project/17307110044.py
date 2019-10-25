#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Project 3 分数排名
# 宋德夫（17307110044）

import project3_util as util

if __name__ == "__main__":
    
    exam_scores = util.generate_exam_scores()
    print("\n总共%d同学分数如下：" % len(exam_scores))
    util.print_scores(exam_scores)
    
    print("\n前10位分数（从高到低）分别为")
    top_10 = sorted(exam_scores)[-10:]
    top_10.reverse()
    util.print_scores(top_10)
            
    print("\n后10位分数（从低到高）分别为")
    bottom_10 = sorted(exam_scores)[:10]
    util.print_scores(bottom_10)

    mean = sum(exam_scores) / len(exam_scores)
    f1 = float(mean)
    print("\n平均分" + "%.1f" % f1)
    
    x = len(exam_scores)
    if x % 2 == 1:
        x0 = (x - 1) * 0.5 + 1
        median = sorted(exam_scores)[int(x0 - 1)]
    elif x % 2 == 0:
        x1 = x * 0.5
        x2 = x * 0.5 + 1
        median = (sorted(exam_scores)[int(x1 - 1)] +
                  sorted(exam_scores)[int(x2 - 1)]) * 0.5
    f2 = float(median)
    print("\n中位数" + "%.1f" % f2 + "\n")

        
    

