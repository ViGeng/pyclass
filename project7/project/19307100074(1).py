#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random
import string

def get_name(min_chars=3, max_chars=8):
    """ 返回一个名字，长度介于min_chars和max_chars之间
    """
    VALID_CHARS = string.ascii_lowercase

    names = [random.choice(VALID_CHARS) for i in range(random.randint(min_chars,max_chars))]
    names[0] = names[0].upper()
    return ''.join(names)


def get_score():
    """ 返回一个分数，介于50和100之间
    """
    return random.randint(50,100)

ids_in_use = []

def get_id():
    """ 返回一个唯一的ID，在[1,999]之间
    """
    global ids_in_use    # 这一行可不要

    while True:
        s_id = random.randint(1, 999)
        if s_id not in ids_in_use:
            ids_in_use.append(s_id)
            return s_id
