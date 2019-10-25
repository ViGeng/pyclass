#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random

def print_scores(scores):
    """ 打印scores中的分数，每行5个数值"""
    count = 0
    for score in scores:
        print(score, end='\t')
        count += 1
        if count % 5 == 0:
            print()
    if count % 5 != 0:
        print()


def generate_exam_scores():
    """ 某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    total = random.randint(45, 90)
    scores = []
    for i in range(total):
        scores.append(random.randint(50, 100))
    return scores