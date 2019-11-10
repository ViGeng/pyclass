#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Project 5 欧拉数 e
# 宋德夫（17307110044）

def main():
    
    e = 0
    t = 1
    x = 1
    
    while t >= 10 ** (-10):
        e = e + t
        t = t / x
        x += 1
        
    print(e)

if __name__ == "__main__":
    main()
