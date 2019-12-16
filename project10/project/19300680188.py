#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import random


def main():
   while True:
      answer = random.randint(1,100)
      for i in range(4):
         f = False
         
         while True:
            try:
               print('[%d]:' % (i+1), end = '')
               number = int(input("您猜的数是?"))
               if 1 <= number <=100:
                  number = int(number)
                  break
               else:
                  print('请输入一个[1,100]范围的整数')
            except ValueError as e:
               print('请输入一个[1,100]范围的整数', e)

         if number > answer:
            print('您猜的数太大了！')
         else:
            if number < answer:
               print('您猜的数太小了！')
            else:
               print('您猜对了！')
               f = True
               break

      if not f:
         print('您已经猜了4次，要猜的数是%d' % answer)
      
      x = input("继续游戏(Y/N)?...")
      if (x != 'Y') and (x != 'y'):
         break
       


if __name__ == '__main__':
    main()
