#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# Project 10 猜数游戏
# 宋德夫（17307110044）

import random

def guess():
    
    while True:
        number = random.randint(1, 100)
        correct = False
        count = 1
        while count <= 4:
            guess_number = input("[" + str(count) + "]:您猜的数是?")
            try:
                guess_number = int(guess_number)
            except ValueError:
                print("请输入一个[1,100]范围的整数")
            else:
                if guess_number < 1 or guess_number > 100:
                    print("请输入一个[1,100]范围的整数")
                    continue
                if number == guess_number:
                    print("您猜对了!")
                    correct = True
                    break
                elif number > guess_number:
                    print("您猜的数太小了!")
                    count += 1
                elif number < guess_number:
                    print("您猜的数太大了!")
                    count += 1 
        if not correct:
            print("您已经猜了4次,要猜的数是" + str(number))
        answer = input("继续游戏(Y/N)?...")
        if answer != "y" and answer != "Y":
            break

def main():
    
    guess()

if __name__ == "__main__":
    main()

