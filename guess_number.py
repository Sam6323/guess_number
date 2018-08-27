import random
num = random.randint(1, 100)
while True:
	guess_num = int(input('請猜數字: '))
	if guess_num == num:
		print('終於猜對了!')
		break
	elif guess_num > num:
		print('你猜的數字比答案大')
	else:
		print('你猜的數字比答案小')