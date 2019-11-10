#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-
  
i = item = 1
total = 1
while i<=10**4:
    item *= i
    total += 1 / item
    i += 1
else:
    print("自然对数的底数e的值约为",total)






