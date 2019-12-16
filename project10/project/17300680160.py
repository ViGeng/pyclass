# -*- coding: utf-8 -*-

import random
 
num = random.randint(1,100)

i = 1
while i < 5:
	guess = input('[' + str(i) + ']' + ':您猜的数是？')
	if guess.isdigit():
		guess = int(guess)
		if 1 <= guess <= 100:
			if guess == num:
				print('恭喜您猜对了')
				break
			elif guess > num:
				print('您猜的数字太大了！')
			else:
				print('您猜的数字太小了！')
			i = i + 1
		else:
			print('请输入一个[1,100]范围的整数')
	else:
		print('请输入一个[1,100]范围的整数')
	i = i
	if i == 5:
		print('您已经猜了4次，要猜的数是' + str(num))
		cont = input('继续游戏？(Y/N)...') 
		if cont == 'Y' or 'y':
			i = 1
		else:
			print("结束游戏")