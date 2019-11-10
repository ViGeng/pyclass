#!/usr/bin/env python3
#  -*- coding: utf-8 -*-

i=item=1
total=1
while item<10**10:
    item *=i
    item=float(item)
    total += 1/item
    i +=1
    
print("自然对数的底数e的值为", total)

