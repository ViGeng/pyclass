#Project 10 19300680271 梁栢澄
import random

def riddle():
    r=random.randint(1,100)
    s=0
    while True:
      try:
          x=input('您猜的数是：')
          y=int(x)
      except ValueError as e:
          print('请输入一个[1,100]范围的整数 invalid literal for int() with base 10:',repr(x))
          continue
      else:
          if y not in range(1,101):
              print('请输入一个[1,100]范围的整数 invalid literal for int() with base 10:',repr(x))
          if y in range(1,r):
              print('您猜的数太小了！')
              s+=1
          if y in range(r+1,101):
              print('您猜的数太大了！')
              s+=1
          if y==r:
              print('您猜对了！')
              break
          if s==4:
              print('您已经猜了四次，要猜的数是%d'%r)
              break

riddle()

z=input('继续游戏(Y/N)?...')
if z=='Y':
    riddle()

            
