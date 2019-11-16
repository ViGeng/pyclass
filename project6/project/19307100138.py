#!/usr/local/bin/python3
#  -*- coding: utf-8 -*-
print("总共有4个解")

for cook in range(0,20):
    for hen in range(0,33):
        if cook * 5 + hen * 3 + (100-cook-hen)/3 == 100 and (100-cook-hen)%3==0:
            print("鸡翁 %d 鸡母 %d 鸡雏 %d"% (cook,hen,(100-cook-hen)))
            

            
