#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

import random
import string

def get_name(min_chars=3, max_chars=8):
    VALID_CHARS = string.ascii_lowercase
    names = [random.choice(VALID_CHARS) for i in range(random.randint(min_chars,max_chars))]
    names[0] = names[0].upper()
    return ''.join(names)

def get_score():
    return random.randint(50,100) 
ids_in_use = []

def get_id():
    while True:
        s_id = random.randint(1, 999)
        if s_id not in ids_in_use:
            ids_in_use.append(s_id)
            return s_id
        
def get_class_sheet(total=25):
    class_sheet = dict() 
    for item in range(total):
        ID = get_id()
        class_sheet[ID] = [get_name(),get_score()]
    return class_sheet

def print_class_sheet(class_sheet):
   
    print ('%6s   %-14s%-5s' % ('ID','Name','Score'))

    d2 = list(class_sheet.items())
    d2 = sorted(d2,key=lambda x:(x[0]))
       
    for i in d2:
        print ('%6d   %-14s%-5d' % (i[0],i[1][0],i[1][1]))        
  


def print_class_sheet_sorted(class_sheet):
    print ('%6s   %-14s%-5s' % ('ID','Name','Score'))   
    d3 = list(class_sheet.items())
    d3 = sorted(d3,key=lambda x:(x[1][1]))
    for i in d3:
        print ('%6d   %-14s%-5d' % (i[0],i[1][0],i[1][1]))   

  

def main():
    class_sheet = get_class_sheet(25)

    print()
    print('成绩单如下，按照ID排序\n') 
    print_class_sheet(class_sheet)

    print() 
    print('-'*50)
    print()
    print('成绩单如下，按照成绩排序\n') 
    
    print_class_sheet_sorted(class_sheet)

if __name__ == '__main__':
    main()
    

